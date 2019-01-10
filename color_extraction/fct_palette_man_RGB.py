# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:31:48 2018

@author: Christelle Cocco
"""

from scipy.misc import imread, imresize
import numpy as np
from skimage import filters

def palette_RGB(image_path, dim_max = 320, dim_filter = 3):
    """
    Function to extract the presence or absence of colours of an image 
    according to the distance between each pixel and a set of defined colours
    """
    img = imread(image_path)
    improp = dim_max/max(img.shape)
    img = imresize(img, improp)
    
    colours = {
           # red
           'red0'    : [255,204,204],
           'red1'    : [255,153,153],
           'red2'    : [255,102,102],
           'red3'    : [255,51 ,51 ],
           'red'     : [255,0  ,0  ],
           'red4'    : [204,0  ,0  ],
           'red5'    : [153,0  ,0  ],
           'red6'    : [102,0  ,0  ],
           'red7'    : [51 ,0  ,0  ],
           # orange, beige and brown
           'orange0' : [255,229,204],
           'orange1' : [255,204,153],
           'orange2' : [255,178,102],
           'orange3' : [255,153,51 ],
           'orange'  : [255,128,0  ],
           'orange4' : [204,102,0  ],
           'orange5' : [153,76 ,0  ],
           'orange6' : [102,51 ,0  ],
           'orange7' : [51 ,25 ,0  ],
           # yellow
           'yellow0' : [255,255,204],
           'yellow1' : [255,255,153],
           'yellow2' : [255,255,102],
           'yellow3' : [255,255,51 ],
           'yellow'  : [255,255,0  ],
           'yellow4' : [204,204,0  ],
           'yellow5' : [153,153,0  ],
           'yellow6' : [102,102,0  ],
           'yellow7' : [51 ,51 ,0  ],
           # yellow-green
           'yel_gr0' : [229,255,204],
           'yel_gr1' : [204,255,153],
           'yel_gr2' : [178,255,102],
           'yel_gr3' : [153,255,51 ],
           'yel_gr'  : [128,255,0  ],
           'yel_gr4' : [102,204,0  ],
           'yel_gr5' : [76 ,153,0  ],
           'yel_gr6' : [51 ,102,0  ],
           'yel_gr7' : [25 ,51 ,0  ],
           # green
           'green0'  : [204,255,204],
           'green1'  : [153,255,153],
           'green2'  : [102,255,102],
           'green3'  : [51 ,255,51 ],
           'green'   : [0  ,255,0  ],
           'green4'  : [0  ,204,0  ],
           'green5'  : [0  ,153,0  ],
           'green6'  : [0  ,102,0  ],
           'green7'  : [0  ,51 ,0  ],
           # between green and sky
           'gr_sky0' : [204,255,229],
           'gr_sky1' : [153,255,204],
           'gr_sky2' : [102,255,178],
           'gr_sky3' : [51 ,255,153],
           'gr_sky'  : [0  ,255,128],
           'gr_sky4' : [0  ,204,102],
           'gr_sky5' : [0  ,153,76 ],
           'gr_sky6' : [0  ,102,51 ],
           'gr_sky7' : [0  ,51 ,25 ],
           # sky (cyan?)
           'sky0'    : [204,255,255],
           'sky1'    : [153,255,255],
           'sky2'    : [102,255,255],
           'sky3'    : [51 ,255,255],
           'sky'     : [0  ,255,255],
           'sky4'    : [0  ,204,204],
           'sky5'    : [0  ,153,153],
           'sky6'    : [0  ,102,102],
           'sky7'    : [0  ,51 ,51 ],
           # between sky and blue
           'sk_bl0' : [204,229,255],
           'sk_bl1' : [153,204,255],
           'sk_bl2' : [102,178,255],
           'sk_bl3' : [51 ,153,255],
           'sk_bl'  : [0  ,128,255],
           'sk_bl4' : [0  ,102,204],
           'sk_bl5' : [0  ,76 ,153],
           'sk_bl6' : [0  ,51 ,102],
           'sk_bl7' : [0  ,25 ,51 ],
           #blue
           'blue0'   : [204,204,255],
           'blue1'   : [153,153,255],
           'blue2'   : [102,102,255],
           'blue3'   : [51 ,51 ,255],
           'blue'    : [0  ,0  ,255],
           'blue4'   : [0  ,0  ,204],
           'blue5'   : [0  ,0  ,153],
           'blue6'   : [0  ,0  ,102],
           'blue7'   : [0  ,0  ,51 ],
           # violet
           'violet0' : [229,204,255],
           'violet1' : [204,153,255],
           'violet2' : [178,102,255],
           'violet3' : [153,51 ,255],
           'violet'  : [127,0  ,255],
           'violet4' : [102,0  ,204],
           'violet5' : [76 ,0  ,153],
           'violet6' : [51 ,0  ,102],
           'violet7' : [25 ,0  ,51 ],
           # fuchsia
           'fuchsia0': [255,204,255],
           'fuchsia1': [255,153,255],
           'fuchsia2': [255,102,255],
           'fuchsia3': [255,51 ,255],
           'fuchsia' : [255,0  ,255],
           'fuchsia4': [204,0  ,204],
           'fuchsia5': [153,0  ,153],
           'fuchsia6': [102,0  ,102],
           'fuchsia7': [51 ,0  ,51 ],
           # pink
           'pink0'   : [255,204,229],
           'pink1'   : [255,153,204],
           'pink2'   : [255,102,178],
           'pink3'   : [255,51 ,153],
           'pink'    : [255,0  ,127],
           'pink4'   : [204,0  ,102],
           'pink5'   : [153,0  ,76 ],
           'pink6'   : [102,0  ,51 ],
           'pink7'   : [51 ,0  ,25 ],
           #white - black
           'white'   : [255,255,255],
           'gray1'   : [224,224,224],
           'gray2'   : [192,192,192],
           'gray3'   : [160,160,160],
           'gray'    : [128,128,128],
           'gray4'   : [96 ,96 ,96 ],
           'gray5'   : [64 ,64 ,64 ],
           'gray6'   : [32 ,32 ,32 ],
           'black'   : [0  ,0  ,0  ],
           }
          
    
    red_dr    = np.zeros((img.shape[0], img.shape[1]))
    orange_dr = np.zeros((img.shape[0], img.shape[1]))
    yellow_dr = np.zeros((img.shape[0], img.shape[1]))
    green_dr  = np.zeros((img.shape[0], img.shape[1]))
    sky_dr    = np.zeros((img.shape[0], img.shape[1]))
    blue_dr   = np.zeros((img.shape[0], img.shape[1]))
    purple_dr = np.zeros((img.shape[0], img.shape[1]))
    pink_dr   = np.zeros((img.shape[0], img.shape[1]))
    white_dr  = np.zeros((img.shape[0], img.shape[1]))
    achro_dr  = np.zeros((img.shape[0], img.shape[1]))
    other_dr  = np.zeros((img.shape[0], img.shape[1]))
    
    for i in range(img.shape[0]):

    
        for j in range(img.shape[1]):
            dist = [((img[i,j][0] - colours[col][0])**2 + 
                      (img[i,j][1] - colours[col][1])**2 + 
                       (img[i,j][2] - colours[col][2])**2) 
            for col in sorted(colours.keys())]
            
            color = sorted(colours.keys())[dist.index(min(dist))]
            
            if color == 'white':
                white_dr[i,j] = 1
            elif color.startswith('red') or color.startswith('pink'):
                red_dr[i,j] = 1
            elif color.startswith('orange'):
                orange_dr[i,j] = 1
            elif color.startswith('yellow'):
                yellow_dr[i,j] = 1
            elif color.startswith('yel_gr') or color.startswith('green') or \
            color.startswith('gr_sky'):
                green_dr[i,j] = 1
            elif color.startswith('sky'):
                sky_dr[i,j] = 1
            elif color.startswith('sk_bl') or color.startswith('blue'):
                blue_dr[i,j] = 1
            elif color.startswith('violet'):
                purple_dr[i,j] = 1
            elif color.startswith('fuchsia'):
                pink_dr[i,j] = 1
            elif color.startswith('gray') or color == 'black':
                achro_dr[i,j] = 1
            else:
                other_dr[i,j] = 1
                
    resultsNOfilter = {
           'white'   : np.sum(white_dr),
           'red'     : np.sum(red_dr), 
           'orange'  : np.sum(orange_dr),
           'yellow'  : np.sum(yellow_dr),
           'green'   : np.sum(green_dr),
           'cyan'    : np.sum(sky_dr),
           'blue'    : np.sum(blue_dr),
           'purple'  : np.sum(purple_dr),
           'pink'    : np.sum(pink_dr),
           'achro'   : np.sum(achro_dr)
#           'other'   : np.sum(other_dr)
           }
            

    white_dr  = filters.median(white_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    red_dr    = filters.median(red_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    orange_dr = filters.median(orange_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    yellow_dr = filters.median(yellow_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    green_dr  = filters.median(green_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    sky_dr    = filters.median(sky_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    blue_dr   = filters.median(blue_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    purple_dr = filters.median(purple_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    pink_dr   = filters.median(pink_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))
    achro_dr  = filters.median(achro_dr.astype(dtype = 'uint8'),
                              selem=np.ones((3,3)))

    results = {
           'white'   : int(np.sum(white_dr)>=1),
           'red'     : int(np.sum(red_dr)>=1), 
           'orange'  : int(np.sum(orange_dr)>=1),
           'yellow'  : int(np.sum(yellow_dr)>=1),
           'green'   : int(np.sum(green_dr)>=1),
           'cyan'    : int(np.sum(sky_dr)>=1),
           'blue'    : int(np.sum(blue_dr)>=1),
           'purple'  : int(np.sum(purple_dr)>=1),
           'pink'    : int(np.sum(pink_dr)>=1),
           'achro'   : int(np.sum(achro_dr)>=1)
           }
           
    #path, file = os.path.split(image_path)
    
    #return(file, results)
    return(resultsNOfilter, results)
    
 