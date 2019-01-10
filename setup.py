from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
        
setup(
    name="color_extraction",
    version="0.1",
    description="A python package for decomposing an image into basic colours",
    long_description=readme(),
    url="http://github.com/***",
    author="Christelle Cocco, Raphael Cere, Aris Xanthos",
    author_email="christelle.cocco@unil.ch",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    packages=["color_extraction"],
    install_requires=[
        "numpy",
        "scipy",
        "skimage",
        "matplotlib"
    ],
    zip_safe=False
)