import numpy as np
import six.moves.urllib as urllib
import glob
import itertools
import zipfile
import matplotlib
import math
import random
import cv2
import io

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from collections import defaultdict
from matplotlib import pyplot as plt
from PIL import Image, ImageOps
from object_detection.utils import ops as utils_ops
from matplotlib.colors import colorConverter
import matplotlib.animation as animation
from matplotlib import style


def show_line_chart(VIOLATION_ARR):
    with open('timeline_data.txt', 'w') as writeFile:
        for f,v in VIOLATION_ARR:
            writeFile.write(str(f).split(".")[0] + "," + str(v) + "\n")

    style.use('fivethirtyeight')
    fig = plt.figure(1)
    ax1 = fig.add_subplot(1, 1, 1)

    graph_data = open('timeline_data.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    
    ax1.plot(xs, ys)

    plt.xlabel("Frame number", fontsize=10)
    plt.ylabel("Number of violation", fontsize=10)
    plt.tick_params(axis='both', labelsize=8)


    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img
