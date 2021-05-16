# =================================================================================================================
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ===================================== Importing Libraries =======================================================
from analyse_area import *
from analyse_timeline import *
from numba import jit, cuda
from object_detection.utils import ops as utils_ops
from PIL import Image
import matplotlib.patches as patches
from matplotlib import pyplot as plt
from collections import defaultdict
from object_detection.utils import visualization_utils as vis_util
from object_detection.utils import label_map_util
import numpy as np
import six.moves.urllib as urllib
import glob
import itertools
import zipfile
import matplotlib
import math
import random
import cv2
import tensorflow.compat.v1 as tf
import tempfile
import os
import shutil
tf.disable_v2_behavior()

import tempfile


matplotlib.use('TkAgg')


# =================================================================================================================
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ===================================== Defining Path & Other Variables ===========================================
IMAGE_OUTPUT_SIZE = (12, 8)
SAFE_DISTANCE = 100  # in pixels

# Frozen Graph of trained models (rfcn_resnet101_coco_2018_01_28, ssd_enceptionv2, ssd_mobilenet_v1_coco_2018_01_28)
# define the model path here
FROZEN_RFCN_GRAPH = "exported/rfcn_exported/frozen_inference_graph.pb"
#FROZEN_SSD_INCEPTION_GRAPH = "ssd_inception_exported/frozen_inference_graph.pb"
#FROZEN_SSD_MOBILENET = "ssd_mobilenet_v1_coco_exported/frozen_inference_graph.pb"

frozen_graph = FROZEN_RFCN_GRAPH  # define the chosen model
# define the label_map.pbtxt path here
label_map = label_map_util.load_labelmap("label_map.pbtxt")

# define the video path here
cap = cv2.VideoCapture('TownCentreXVID.mp4')

FILE_OUTPUT = 'temp/tempVideo.avi'

width = int(cap.get(3))
height = int(cap.get(4))
dim = (width, height)


# =================================================================================================================
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ===================================== Loading the frozen graph and label map ====================================
detection_graph = tf.Graph()

with detection_graph.as_default():
    graph_def = tf.GraphDef()
    with tf.gfile.GFile(frozen_graph, 'rb') as fid:
        serialized_graph = fid.read()
        graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(graph_def, name='')

categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=1, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# =================================================================================================================
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ================== Functions of Calculating distance between centroids of each predicted boxes ==================
# Convert image to numpy array
def image_to_numpy_array(image):
    (real_width, real_height) = image.size
    return np.array(image.getdata()).reshape((real_height, real_width, 3)).astype(np.uint8)

# Get the coordinates for each object


def calculate_coordinates(box, width, height):
    xmin = box[1] * width
    ymin = box[0] * height
    xmax = box[3] * width
    ymax = box[2] * height
    return [xmin, ymin, xmax - xmin, ymax - ymin]

# Calculate all possible permutations between centroids


def calculate_permutation(centroids):
    permutations = []
    for permutation in itertools.permutations(centroids, 2):
        if permutation[::-1] not in permutations:
            permutations.append(permutation)
    return permutations


# =================================================================================================================
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ================ Predicting person objects in each frame and displaying it as a real time video =================


def run_inference():
    with detection_graph.as_default():
        with tf.Session() as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name(
                'detection_boxes:0')

            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name(
                'detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name(
                'detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name(
                'num_detections:0')

            tope = 10
            new = True
            VIOLATION_ARR = []
            ALL_CENTROIDS = []
            while(cap.isOpened()):
                # Capture frame-by-frame
                ret, frame = cap.read()
                frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)

                if ret == True:
                    violation = 0
                    # Correct color
                    frame = gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    operations = tf.get_default_graph().get_operations()
                    tensor_names = {
                        output.name for operation in operations for output in operation.outputs}
                    tensor_dict = {}

                    for key in ['num_detections', 'detection_boxes', 'detection_scores', 'detection_classes', 'detection_masks']:
                        tensor = key + ":0"
                        if tensor in tensor_names:
                            tensor_dict[key] = tf.get_default_graph(
                            ).get_tensor_by_name(tensor)

                    if 'detection_masks' in tensor_dict:
                        detection_boxes = tf.squeeze(
                            tensor_dict['detection_boxes'], [0])
                        detection_masks = tf.squeeze(
                            tensor_dict['num_detections'], [0])
                        num_detection = tf.cast(
                            tensor_dict['num_detections'][0], tf.int32)
                        detection_boxes = tf.slice(
                            detection_boxes, [0, 0], [num_detection, -1])
                        detection_masks = tf.slice(detection_masks, [0, 0, 0], [
                                                   num_detection, -1, -1])
                        detection_masks = util_ops.reframe_box_masks_to_image_masks(
                            detection_masks, detection_boxes, image.shape[0], image.shape[1])
                        detection_masks = tf.cast(
                            tf.greater(detection_masks, 0.5), tf.uint8)
                        tensor_dict['detection_masks'] = tf.expand_dims(
                            detection_masks, 0)

                    # Actual detection.
                    output_dict = sess.run(tensor_dict, feed_dict={
                                           image_tensor: np.expand_dims(frame, 0)})  # The image is from parameter
                    output_dict['num_detections'] = int(
                        output_dict['num_detections'][0])
                    output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(
                        np.uint8)
                    output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
                    output_dict['detection_scores'] = output_dict['detection_scores'][0]

                    if 'detection_masks' in output_dict:
                        output_dict['detection_masks'] = output_dict['detection_masks'][0]

                    # Calculate normalized coordinates for boxes
                    centroids = []
                    coordinates = []
                    for box in output_dict['detection_boxes']:
                        coordinate = calculate_coordinates(box, width, height)

                        #[xmin, ymin, xmax - xmin, ymax - ymin]
                        centroid = (
                            coordinate[0] + (coordinate[2]/2), coordinate[1] + (coordinate[3]/2))
                        centroids.append(centroid)
                        coordinates.append(coordinate)

                    permutations = calculate_permutation(centroids)

                    # Display boxes and centroids
                    fig, axis = plt.subplots(
                        figsize=(10, 6), dpi=90, frameon=False)
                    for coordinate, centroid in zip(coordinates, centroids):
                        plt.axis('off')
                        axis.add_patch(matplotlib.patches.Rectangle(
                            (coordinate[0], coordinate[1]), coordinate[2], coordinate[3], linewidth=1, edgecolor='yellow', facecolor='none', zorder=10))
                        axis.add_patch(matplotlib.patches.Circle(
                            (centroid[0], centroid[1]), 3, color='yellow', zorder=20))

                        # Add the centroids for the area analysis
                        ALL_CENTROIDS.append(centroid)

                    # Display lines between centroids
                    for permutation in permutations:
                        x1 = permutation[0][0]
                        x2 = permutation[1][0]
                        y1 = permutation[0][1]
                        y2 = permutation[1][1]

                        # Calculate the distance between 2 centroids
                        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        average_distance = distance/SAFE_DISTANCE

                        # Calculate middle point
                        middle = ((x1 + x2)/2, (y1 + y2)/2)

                        # Calculate slope
                        if(x2-x1 > 0):
                            slope = (y2-y1)/(x2-x1)
                        else:
                            slope = (y2-y1)

                        dy = math.sqrt(3**2 / (slope**2 + 1))
                        dx = -slope * dy

                        # Set random location
                        if random.randint(1, 10) % 2 == 0:
                            dx = middle[0] - dx*10
                            dy = middle[1] - dy*10
                        else:
                            dx = middle[0] + dx*10
                            dy = middle[1] + dy*10

                        if average_distance < 2:
                            violation = violation + 1
                            axis.annotate((round(average_distance, 2)), xy=middle, color='white', xytext=(
                                dx, dy), fontsize=10, bbox=dict(facecolor='red', edgecolor='white', boxstyle='round', pad=0.2), zorder=30)
                            axis.plot((x1, x2), (y1, y2), linewidth=2,
                                      color='red', zorder=15)
                        else:
                            pass

                    axis.imshow(frame, interpolation='nearest')
                    VIOLATION_ARR.append([frame_number, violation])

                    fig.canvas.draw()  # Convert figure to numpy

                    img = np.fromstring(
                        fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
                    img = img.reshape(
                        fig.canvas.get_width_height()[::-1] + (3,))

                    img = np.array(fig.canvas.get_renderer()._renderer)
                    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                    # Display frames continuosly until 'esc' button has been pressed
                    # cv2.imshow('LIVE', img)
                    # show_line_chart(VIOLATION_ARR)
                    # key = cv2.waitKey(1)

                    if new:
                        print("Define out")
                        out = cv2.VideoWriter(FILE_OUTPUT, cv2.VideoWriter_fourcc(
                            *'XVID'), 20.0, (img.shape[1], img.shape[0]))
                        new = False

                    out.write(img)

                else:
                    break

                    # Press esc key to stop the real time video
                    # if(key == 27):
                    # break

                # <<< Call the analyse area >>>

        cap.release()
        out.release()
# =================================================================================================================
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ======================== Run the program. Press 'esc' key on your keyboard to stop. =============================

 # When everything done, release the video capture and video write objects


run_inference()
cv2.destroyAllWindows()
