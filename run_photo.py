#================================================= LIBRARIES =====================================================
import numpy as np
import six.moves.urllib as urllib
import glob
import itertools
import zipfile
import matplotlib
import math
import random
import cv2
import tensorflow as tf

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from collections import defaultdict
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from object_detection.utils import ops as utils_ops
from numba import jit, cuda

matplotlib.use('TkAgg')
#=================================================================================================================
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#===================================== Define Path and other variables ===========================================
def predict_photo(frozen_graph, image):
  IMAGE_OUTPUT_SIZE = (12, 8)
  SAFE_DISTANCE = 100 #in pixels
  VIOLATION_ARR = []

  #FROZEN_RFCN_GRAPH = "predicted_video/frozen_inference_graph.pb"
  #FROZEN_SSD_INCEPTION_GRAPH = "/content/drive/MyDrive/SocialDistancing/Models/exported/ssd_inception_exported/frozen_inference_graph.pb"
  #FROZEN_SSD_MOBILENET = ""

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

  categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1, use_display_name=True)
  category_index = label_map_util.create_category_index(categories)
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
  # Indexer (to iterate the array)
  limit = 0;

  #The values that we count manually
  #real_violation = [10, 10, 6, 11, 7]

  #(n-1)*n, where n is the number of person in the image
  #all_connection = [462, 380, 272, 342, 306]

  #The pictures that we take are 6120, 6217, 6257, 6436, 6800
  #frames = [6120, 6217, 6257, 6436, 6800]

  #To count for the number of violation that happens in each picture
  violation = 0

  #To count for the number of distance that do not violate the minimum distance
  negative_count = 0

  # Load the image
  image = Image.open(image)
  width, height = image.size

  # Bird's eye view key points
  # corners = np.array([[0, 445], [421, 540], [728, 0], [915, 0]], dtype=np.float32)

  #Inverse Perspective Mapping (IPM) --> Remove perspective effect by remapping the image, resulting a top-down view.
  # ipm_params = np.array([[360,height],[540,height],[360,0],[540,0]], dtype=np.float32)
  # ipm_matrix = cv2.getPerspectiveTransform(corners, ipm_params)
  
  # change to numpy array
  image_np = image_to_numpy_array(image)

  # Turn this on to see the bird's eye view
  #image_np = cv2.warpPerspective(image_np, ipm_matrix, (width, height))

  # Get the output dict
  output_dict = run_inference(image_np, detection_graph)

  # Find the centroids and the coordinates for each box
  centroids = []
  coordinates = []
  for box in output_dict['detection_boxes']:
      coordinate = calculate_coordinates(box, width, height)

      #[xmin, ymin, xmax - xmin, ymax - ymin]
      centroid = (coordinate[0] + (coordinate[2]/2), coordinate[1] + (coordinate[3]/2))

      # To find the ground of the box
      #centroid = list(centroid)
      #centroid[1] = centroid[1] + ((coordinate[3] - coordinate[1])/2)
      #centroid = tuple(centroid)

      centroids.append(centroid)
      coordinates.append(coordinate)

  # Find the permutation of the list of centroids
  permutations = calculate_permutation(centroids)

  # Show the image
  fig, axis = plt.subplots(figsize = (10, 6), dpi=90)
  axis.imshow(image_np, interpolation='nearest')
  # axis.text(20, height-70, "Real number of violations: {}".format(real_violation[limit]))

  # Draw the boxes and centroids
  for coordinate, centroid in zip(coordinates, centroids):
      plt.axis('off')
      axis.add_patch(matplotlib.patches.Rectangle((coordinate[0], coordinate[1]), coordinate[2], coordinate[3], linewidth=1, edgecolor='yellow', facecolor='none', zorder=10))
      axis.add_patch(matplotlib.patches.Circle((centroid[0], centroid[1]), 3, color='yellow', zorder=20))
      
  # Draw the line and count the distance
  for permutation in permutations:
      x1 = permutation[0][0]
      x2 = permutation[1][0]
      y1 = permutation[0][1]
      y2 = permutation[1][1]

      distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
      average_distance = distance/SAFE_DISTANCE
      middle = ((x1 + x2)/2, (y1 + y2)/2)

      if(x2-x1 > 0):
          slope = (y2-y1)/(x2-x1)
      else:
          slope = (y2-y1)

      dy = math.sqrt(3**2 / (slope**2 + 1))
      dx = -slope * dy

      if random.randint(1, 10) % 2 == 0:
          dx = middle[0] - dx*10
          dy = middle[1] - dy*10
      else:
          dx = middle[0] + dx*10
          dy = middle[1] + dy*10

      if average_distance < 2:
          violation = violation + 1
          axis.annotate((round(average_distance, 2)), xy=middle, color='white', xytext=(dx, dy), fontsize=10, bbox=dict(facecolor='red', edgecolor='white', boxstyle='round', pad=0.2), zorder=30)
          axis.plot((x1, x2), (y1, y2), linewidth=2, color='red', zorder=15)
      else:
          negative_count = negative_count + 1
  
  #------------------------------------------------
  # Show the performance of the model
  #------------------------------------------------
  # FN --> Detected as no violation where violation exist
  # TP --> Detected as violation and violation exists
  # Precision = TP / (TP + FP)
  # Recall = TP / (TP + FN)
  #-----------------------------------------------
  # axis.text(20, height-55, "Number of violation detected: {}".format(violation))
  
  # FN = negative_count - (all_connection[limit] - real_violation[limit])

  # Precision = real_violation[limit] / violation
  # Recall = real_violation[limit] / (real_violation[limit] + FN)
  # F1 = 2 * ((Precision * Recall)/(Precision + Recall))

  # axis.text(20, height-40, "Precision: {}".format(Precision))
  # axis.text(20, height-25, "Recall: {}".format(Recall))
  # axis.text(20, height-10, "F1 Score: {}".format(F1))

  #------------------------------------------------
  # Show and save the predicted picture
  #------------------------------------------------
  # plt.tight_layout()
  # plt.show(block=False)
  # plt.pause(3)
  return axis
#============================================================================================================================