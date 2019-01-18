# Color-extraction

Color-extraction is an open-source python module which attributes, to each element of an ndarray
(RGB image) the most similar color from a palette of predefined colors.

Three functions are included in this module ([`get_bool_arrays`](#function-boolean-ndarray), `get_rgb_arrays` and `get_counts`) which, respectively, return a
boolean ndarray for each color, a rgb array for each color and the count of pixels for each color.


## Getting Started

[comment]: <> (These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.)

### Prerequisites

* pathlib.Path
* os
* time
* json
* scipy.cluster.vq
* skimage.filters
* numpy


```
Give examples
```

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

A predefined set of colors is available with ten colors: red,
orange, yellow, green, cyan, blue, purple, pink, achromatic (gray and black),
and white.




### Function boolean ndarray

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
* [Raphaël Ceré](https://github.com/raphaelcere)
* [Aris Xanthos](https://github.com/axanthos) - current version

<!---
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
-->

## Credits
This module was partially funded by the the Swiss National Science Foundation (SNSF), grant N° CR11I1_156383.

The current version was implemented by Aris Xanthos and is based on the original code by Christelle Cocco available [here](color_extraction/fct_palette_man_RGB.py),

To cite this module: en attendant comhum... ;)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
<!---
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->
