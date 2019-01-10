from context import color_extraction
from scipy.misc import imread
import matplotlib.image
import os


WORKING_PATH = os.getcwd()
image_path     = WORKING_PATH+"/demo/Comic_mural_Le_jeune_Albert_Yves_Chaland_Bruxelles.jpg"
output_path    = WORKING_PATH+"/demo/"
color_def_path = "color_definitions.json"

img = imread(image_path)

# to get a boolean array per colour whose the value is true 
dict_bool_arrays          = color_extraction.get_bool_arrays(img)

dict_bool_arrays_median   = color_extraction.get_bool_arrays(img, median_filter = True)

dict_bool_arrays_colordef = color_extraction.get_bool_arrays(img, color_def_path = color_def_path)

# if you need the original file color_definitions.json, you can download it on ...


# output the colours, with no
dict_rgb_arrays = color_extraction.get_rgb_arrays(img)

for color in dict_rgb_arrays.keys():
    matplotlib.image.imsave(output_path+color, dict_rgb_arrays[color])

#
dict_counts_arrays = color_extraction.get_counts(img)
