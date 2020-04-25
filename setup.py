from setuptools import setup

# def readme():
#     with open('README.md') as f:
#         return f.read()

with open('README.md') as f:
    long_description = f.read()
        
setup(
    name="color_extraction",
    version="0.1a4",
    description="A python package for decomposing an image into basic colours",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ChrisCocco/ddd_colours",
    author="Christelle Cocco, Raphael Cere, Aris Xanthos",
    author_email="christelle.cocco@unil.ch",
    license="GPLv3+",
    classifiers=[
        "Development Status :: 4 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    packages=["color_extraction"],
    install_requires=[
        "numpy",
        "scipy",
        "scikit-image",
        "matplotlib"
    ],
    include_package_data=True,
    zip_safe=False
)