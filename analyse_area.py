#================================================= LIBRARIES =====================================================
from matplotlib.figure import Figure
import numpy as np
import itertools
import matplotlib
import math
import random
import tensorflow as tf
import io

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from object_detection.utils import ops as utils_ops
from numba import jit, cuda
from PyQt5.QtGui import QImage, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use('TkAgg')
#=================================================================================================================
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#===================================== Define Path and other variables ===========================================
IMAGE_OUTPUT_SIZE = (12, 8)
SAFE_DISTANCE = 100 #in pixels
VIOLATION_ARR = []

def mask_area(frozen_graph, image):
  frozen_graph
  label_map = label_map_util.load_labelmap("label_map.pbtxt")
  #==============================================================================================================
  #//////////////////////////////////////////////////////////////////////////////////////////////////////////////
  #============================== Load the frozen graph and label map ===========================================
  detection_graph = tf.Graph()

  with detection_graph.as_default():
    graph_def = tf.GraphDef()
    with tf.gfile.GFile(frozen_graph, 'rb') as fid:
      serialized_graph = fid.read()
      graph_def.ParseFromString(serialized_graph)
      tf.import_graph_def(graph_def, name='')

  #==============================================================================================================
  #//////////////////////////////////////////////////////////////////////////////////////////////////////////////
  #==================================== Calculation process =====================================================
  def image_to_numpy_array(image):
    (real_width, real_height) = image.size
    return np.array(image.getdata()).reshape((real_height, real_width, 3)).astype(np.uint8)

  def calculate_coordinates(box, width, height):
    xmin = box[1] * width
    ymin = box[0] * height
    xmax = box[3] * width
    ymax = box[2] * height
    return [xmin, ymin, xmax - xmin, ymax - ymin]

  def calculate_permutation(centroids):
    permutations = []
    for permutation in itertools.permutations(centroids, 2):
      if permutation[::-1] not in permutations:
        permutations.append(permutation)
    return permutations
  #==============================================================================================================
  #//////////////////////////////////////////////////////////////////////////////////////////////////////////////
  #=================================== Inference ================================================================
  '''
  Param:
      image: numpy array of the images
      graph: frozen graph that has been loaded
  Return: tensor_dict --> consists of boxes, masks, etc.    
  '''
  def run_inference(image, graph):
    with graph.as_default():
      with tf.Session() as sess:
        operations = tf.get_default_graph().get_operations()
        tensor_names = {output.name for operation in operations for output in operation.outputs}
        tensor_dict = {}
        for key in ['num_detections', 'detection_boxes', 'detection_scores', 'detection_classes', 'detection_masks']:
          tensor = key + ":0"
          if tensor in tensor_names:
            tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor)
        if 'detection_masks' in tensor_dict:
          detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
          detection_masks = tf.squeeze(tensor_dict['num_detections'], [0])
          num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
          
          detection_boxes = tf.slice(detection_boxes, [0,0], [num_detection, -1])
          
          detection_masks = tf.slice(detection_masks, [0, 0, 0], [num_detection, -1, -1])
          detection_masks = util_ops.reframe_box_masks_to_image_masks(detection_masks, detection_boxes, image.shape[0], image.shape[1])
          detection_masks = tf.cast(tf.greater(detection_masks, 0.5), tf.uint8)
          tensor_dict['detection_masks'] = tf.expand_dims(detection_masks, 0)
        
        image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

        output_dict = sess.run(tensor_dict, feed_dict={image_tensor: np.expand_dims(image, 0)}) #The image is from parameter
        output_dict['num_detections'] = int(output_dict['num_detections'][0])
        output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(np.uint8)
        output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
        output_dict['detection_scores'] = output_dict['detection_scores'][0]
        if 'detection_masks' in output_dict:
          output_dict['detection_masks'] = output_dict['detection_masks'][0]
    
    return output_dict
  #============================================================================================================================
  #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  #============================================== Entrance ====================================================================
  # Load the image
  image = Image.open(image)
  width, height = image.size

  # change to numpy array
  image_np = image_to_numpy_array(image)

  # Show the grayscale color for better interface
  image_gray = image.convert("L")
  image_gray = np.array(image_gray)

  # Get the output dict
  output_dict = run_inference(image_np, detection_graph)

  # Find the centroids and the coordinates for each box
  centroids = []
  coordinates = []
  for box in output_dict['detection_boxes']:
      coordinate = calculate_coordinates(box, width, height)

      #[xmin, ymin, xmax - xmin, ymax - ymin]
      centroid = (coordinate[0] + (coordinate[2]/2), coordinate[1] + (coordinate[3]/2))

      centroids.append(centroid)
      coordinates.append(coordinate)

  # Find the permutation of the list of centroids
  permutations = calculate_permutation(centroids)

  # ------------------ Draw the area that has violation ------------------------
  fig, axis = plt.subplots(figsize = (12, 8), dpi = 90)
  axis.imshow(image_gray, cmap='gray', vmin=0, vmax=255, interpolation='none')

  for coordinate, centroid in zip(coordinates, centroids):
    plt.axis('off')
    for permutation in permutations:
        x1 = permutation[0][0]
        x2 = permutation[1][0]
        y1 = permutation[0][1]
        y2 = permutation[1][1]

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        average_distance = distance/SAFE_DISTANCE
        
        if average_distance < 2:
          axis.add_patch(matplotlib.patches.Circle((centroid[0], centroid[1]), 70, facecolor='#FF000001', zorder=20))
  #------------------------------------------------------------------------------

  #------------------------------------------------
  # Return the analyzed picture
  #------------------------------------------------
  buf = io.BytesIO()
  plt.tight_layout()
  plt.savefig(buf)
  buf.seek(0)
  img = Image.open(buf)
  return img
#============================================================================================================================