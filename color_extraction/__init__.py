# -*- coding: utf-8 -*-
"""TODO: docstring
"""

from pathlib import Path
import time
import json

from scipy.misc import imread
from scipy.cluster.vq import vq
from skimage import filters
import numpy as np
import matplotlib

# TODO...
__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"
start_time = time.clock()

# Parameters
image_folder = Path("")
image_name = Path("test.jpg")
save_path = Path("color_extract")
color_config = Path("color_definitions.json")
median_filter = True

try:
    with open(color_config) as json_file:  
        color_definitions = json.load(json_file)
except IOError:
    print("Couldn't read file %s" % color_config)

color_names = list()
color_vectors = list()
for color_name, color_vector_list in color_definitions.items():
    for color_vector in color_vector_list:
        color_names.append(color_name)
        color_vectors.append(color_vector)
code_book = np.array(color_vectors)

image_path = image_folder / image_name
img = imread(image_path)
w, h, d = img.shape
assert d == 3

image_array = np.reshape(img, (w * h, d))
labels, _ = vq(image_array, code_book)
img_labels = np.empty((w * h), dtype=object)
for idx, label in np.ndenumerate(labels):
    img_labels[idx] = color_names[label]
img_labels = np.reshape(img_labels, (w, h))

bool_matrices = dict()
for color_name in set(color_names):
    bool_matrices[color_name] = img_labels == color_name
    if median_filter:
        bool_matrix = filters.median(
            bool_matrices[color_name].astype(dtype = 'uint8'),
            selem=np.ones((3,3)),
        ).astype(dtype = 'bool')
    else:
        bool_matrix = bool_matrices[color_name]
    viz = img.copy()
    viz[np.invert(bool_matrix)] = 0
    output_path = save_path / Path('%s.png' % color_name)
    matplotlib.image.imsave(output_path, viz)
    print(color_name, np.sum(bool_matrix))

print("--- %s seconds ---" % (time.clock() - start_time))