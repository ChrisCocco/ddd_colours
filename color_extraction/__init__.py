# -*- coding: utf-8 -*-
"""Colors_extraction : this module attributes to each element of an ndarray 
(RGB image) the most similar color from a palette of predefined colors: red, 
orange, yellow, green, cyan, blue, purple, pink, achromatic (gray and black), 
and white.
"""

from pathlib import Path
import os
import time
import json

from scipy.cluster.vq import vq
from skimage import filters
import numpy as np

__author__ = "Christelle Cocco, Aris Xanthos, and Raphael Cere"
__copyright__ = "Copyright 2019, University of Lausanne, Switzerland"
__credits__ = ["Christelle Cocco", "Aris Xanthos", "Raphael Cere"]
__license__ = "GNU GPLv3"
__version__ = "0.1a0"
__maintainer__ = "Christelle Cocco"
__email__ = "Christelle.Cocco@unil.ch"
__status__ = "Development"

# Parameters...


BASE_PATH  = os.path.dirname(os.path.abspath(__file__))
def get_data(path):
    return BASE_PATH+'/color_definitions.json'


def load_color_definitions(path=BASE_PATH):
    """Given a path to a JSON file, load color definitions from this file.

    Args:
        path (string): the path to the color definition file.

    Returns:
        list: list of color names.
        list: list of RGB color vectors (centroids).

    """
    # Open and read color definition file...
    COLOR_DEF_PATH = get_data(BASE_PATH)
    try:
        with open(COLOR_DEF_PATH) as json_file:  
            color_definitions = json.load(json_file)
    except IOError:
        raise IOError("Couldn't read color definition file %s" % COLOR_DEF_PATH)

    # Store list of color names and color vectors (centroids)...
    color_names = list()
    color_vectors = list()
    for color_name, color_vector_list in color_definitions.items():
        for color_vector in color_vector_list:
            color_names.append(color_name)
            color_vectors.append(color_vector)
    code_book = np.array(color_vectors)
    
    return code_book, color_names

# Load default color definitions.
CODE_BOOK, COLOR_NAMES = load_color_definitions()

def get_bool_arrays(image, median_filter=False, color_def_path=None):
    """Given an RGB image (array), return a dictionary where each key is a basic 
    color name and each value is a boolean array with the same dimensions as the 
    image, indicating whether the color in question has been detected at each 
    position of the image.

    Args:
        image (ndarray): the input RGB image as a numpy array.
        median_filter (bool): whether a 3x3 median filter should be applied 
        color_def_path (string): path to a custom JSON color definition file

    Returns:
        dict: dictionary with color_names (strings) as keys and boolean arrays
        as values.

    """
    # Load custom color definitions if required...
    if color_def_path:
        code_book, color_names = load_color_definitions()
    else:
        code_book, color_names = CODE_BOOK, COLOR_NAMES
    
    # Get color label array...
    w, h, d = image.shape
    assert d >= 3, "Image doesn't have 3 dimensions, please make sure it is RGB. By default, the 4th dimension is ignored if the format is RGBA,"
    image_array = np.reshape(image[:,:,:3], (w * h, 3))
    assert max(image_array[:,1]) <= 1.0, "The RGB triplet value is not in 0-255 range, please make sure it is RGB. By default, the 0-1 range is rescaled to 0-255."
    if max(image_array[:,1]) <= 1.0:
        image_array = image_array*255
    labels, _ = vq(image_array, code_book)
    img_labels = np.empty((w * h), dtype=object)
    for idx, label in np.ndenumerate(labels):
        img_labels[idx] = color_names[label]
    img_labels = np.reshape(img_labels, (w, h))

    # Create color bool arrays and store in dictionary...
    bool_arrays = dict()
    for color_name in set(color_names):
        bool_array = img_labels == color_name
        if median_filter:
            bool_arrays[color_name] = filters.median(
                bool_array.astype(dtype = 'uint8'),
                selem=np.ones((3,3)),
            ).astype(dtype = 'bool')
        else:
            bool_arrays[color_name] = bool_array

    return bool_arrays

def get_rgb_arrays(image, median_filter=False, color_def_path=None):
    """Given an RGB image (array), return a dictionary where each key is a basic 
    color name and each value is a RGB array with the same dimensions as the 
    image. Positions where the color in question has been detected contain the
    original RGB color found in the input image; other positions have the value
    0 (black), or 1 (white) in the case of the "achro(matic)" color.

    Args:
        image (ndarray): the input RGB image as a numpy array.
        median_filter (bool): whether a 3x3 median filter should be applied 
        color_def_path (string): path to a custom JSON color definition file

    Returns:
        dict: dictionary with color_names (strings) as keys and RGB arrays
        as values.

    """
    # Get bool arrays...
    bool_arrays = get_bool_arrays(image, median_filter, color_def_path)
    
    # Convert bool to rgb...
    rgb_arrays = dict()
    for color_name in bool_arrays:
        rgb_arrays[color_name] = image.copy()
        bg_color = 255 if color_name == "achro" else 0
        rgb_arrays[color_name][np.invert(bool_arrays[color_name])] = bg_color

    return rgb_arrays
        
def get_counts(image, color_def_path=None):
    """Given an RGB image (array), return a dictionary where each key is a basic 
    color name and each value is the count of the number of pixels with this
    color in the image.

    Args:
        image (ndarray): the input RGB image as a numpy array.
        color_def_path (string): path to a custom JSON color definition file

    Returns:
        dict: dictionary with color_names (strings) as keys and integer values.

    """
    # Get bool arrays...
    bool_arrays = get_bool_arrays(image, median_filter=False, color_def_path=color_def_path)

    # Count pixels in bool arrays...
    counts = dict()
    for color_name in bool_arrays:
        counts[color_name] = np.sum(bool_arrays[color_name])

    return counts

