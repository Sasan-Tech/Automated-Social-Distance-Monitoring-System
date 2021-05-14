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

'''

Note:
Take all the centroids that have been saved into an array from the video
Draw all the centroids to a certain image

The code below need to be refactored right after the load video function works properly

NOT DONE YET. CANNOT RUN!

'''

def mask_area(ALL_CENTROIDS, image):
  #============================================================================================================================
  #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  #============================================== Entrance ====================================================================
  # Load the image
  width, height = image.size

  # Show the grayscale color for better interface
  image_gray = image.convert("L")
  image_gray = np.array(image_gray)

  # ------------------ Mask the area ------------------------
  fig, axis = plt.subplots(figsize = (12, 8), dpi = 90)
  axis.imshow(image_gray, cmap='gray', vmin=0, vmax=255, interpolation='none')

  for centroid in ALL_CENTROIDS:
    plt.axis('off')
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