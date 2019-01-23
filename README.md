# Color-extraction

Color-extraction is an open-source python module which attributes to each element of an ndarray (RGB image) the most similar color from a palette of predefined colors.

Three functions are included in this module: [`get_bool_arrays`](#boolean-array), [`get_rgb_arrays`](#rgb-arrays) and [`get_counts`](#counts) which, respectively, return a
boolean ndarray for each color, a rgb array for each color and the count of pixels for each color.

[comment]: <> (## Getting Started RC: pas nécessaire)

[comment]: <> (These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. RC: pas nécessaire)

## Requirements

* pathlib.Path
* os
* time
* json
* scipy.cluster.vq
* skimage.filters
* numpy


[comment]: <> (```Give examples```)

### Installing

```
pip install color_extraction
```

<!---
## Running the tests

Explain how to run the automated tests for this system ????

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With ???

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

-->

## Usage examples

A predefined set of colors is included in the module with ten colors: red,
orange, yellow, green, cyan, blue, purple, pink, achromatic (gray and black),
and white. This set of colors, which can be modified, is available at
[https://github.com/ChrisCocco/ddd_colours/blob/master/color_extraction/color_definitions.json](https://github.com/ChrisCocco/ddd_colours/blob/master/color_extraction/color_definitions.json).

To start:
```
import color_extraction
from scipy.misc import imread

img = imread(image_path)
```

[comment]: <> (RC: Comme il y a la demo dams le package, peut-être qu'il faudrait simplement dire coment lancer cette demo ici et ensuite on peut donner des détails comme ici-desous.)

### Boolean array

[comment]: <> (RC: Je ne suis convaincu que ce soit nécessaire de donner l'output de cet exemple comme on dit déjà dans l'intro que cette fonction une ndarray bool poour chque couleur. Ce qui retourne ce que l'on appelle un mask par couleur.)

The function `get_bool_arrays` returns a dictionary with a boolean ndarray for
each color.

```
>>> dict_bool_arrays          = color_extraction.get_bool_arrays(img)

>>> dict_bool_arrays
{'white': array([[False, False, False, ...,  True,  True,  True],
       [False, False, False, ...,  True,  True,  True],
       [False, False, False, ...,  True,  True,  True],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]], dtype=bool), 'yellow': array([[False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]], dtype=bool), ...}
```


[comment]: <> (RC:  Ci-dessous ce sont les arguments de la fonction, peut-être reduire ceci à un paragraphe?)  
It is also possible to use a median filter (3 x 3).

```
color_extraction.get_bool_arrays(img, median_filter = True)
```

Or to use your own color definition set saved in a JSON file.

```
color_extraction.get_bool_arrays(img, color_def_path = your_file_path/filename.json)
```

### RGB arrays

The function `get_rgb_arrays` returns a dictionary with a RGB array for each color. Especially, positions where the color in question has been detected contain the original RGB color found in the input image; other positions have the value 0 (black), except in the case of the "achro(matic)" color where other position have the value 1 (white).

```
import matplotlib.image

dict_rgb_arrays = color_extraction.get_rgb_arrays(img)

for color in dict_rgb_arrays.keys():
    matplotlib.image.imsave(output_path+color, dict_rgb_arrays[color])

```

The results for this image:
![Original image](tests/demo/Comic_mural_Le_jeune_Albert_Yves_Chaland_Bruxelles.jpg)

Are:

* For white:
![White](tests/demo/white.png)

* For red:
![Red](tests/demo/red.png)

* For orange:
![Orange](tests/demo/orange.png)

* For yellow:
![Yellow](tests/demo/yellow.png)

* For green:
![Green](tests/demo/green.png)

* For cyan:
![Cyan](tests/demo/cyan.png)

* For blue:
![Blue](tests/demo/blue.png)

* For purple:
![Purple](tests/demo/purple.png)

* For pink:
![White](tests/demo/pink.png)

* For achromatic:
![Achromatic](tests/demo/achro.png)



As for the boolean matrix, it is possible to use a median filter or your own color definition set, with the same parameters.

### Counts

The function `get_counts` returns a dictionary with the number of pixels of each colour.

```
>>> dict_counts_arrays = color_extraction.get_counts(img)

>>> dict_counts_arrays
{'purple': 25, 'blue': 6652, 'achro': 2477505, 'cyan': 764, 'white': 9567, 'green': 185, 'red': 114555, 'pink': 163, 'orange': 150263, 'yellow': 5121}
```

As for the boolean matrix, it is possible to use a median filter or your own color definition set, with the same parameters.

<!---
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. ????
-->

<!---
## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). ????
-->

## Authors

* [Christelle Cocco](https://github.com/ChrisCocco) - initial work
* [Raphaël Ceré](https://github.com/raphaelcere) - contributor
* [Aris Xanthos](https://github.com/axanthos) - current version

<!---
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
-->

## Credits
This module was partially funded by the the Swiss National Science Foundation (SNSF), grant N° CR11I1_156383.

The current version was implemented by Aris Xanthos and is based on the original code by Christelle Cocco available [here](color_extraction/fct_palette_man_RGB.py),

To cite this module: en attendant comhum... ;)


## License

This project is licensed under the MIT License (VRAIMENT? AUSSI DANS SETUP) - see the [LICENSE](LICENSE) file for details
<!---
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->
