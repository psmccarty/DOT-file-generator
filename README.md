# DOT-file-generator
A DOT (graph description language) dataset generator

## Description

Need a dataset for a graph related algorithm assignment? I got you covered! dotConverter.py uses pygraphviz to convert a subset of the worldcities.csv found in https://simplemaps.com/data/world-cities into a valid DOT file suitable for all your graph needs. You are also welcome to use the prebuilt dot files I have made.

## Getting Started

### Dependencies
To use this program you will need pygraphviz. The installation give can by found on their website: [pygraphviz](https://pygraphviz.github.io/documentation/stable/install.html#windows-install)

### Excecuting program on Linux
* Be in a directory with dotConverter.py, worldcities.csv, a CSV file with the city names and city IDs of the nodes in your graph, and a CSV with the edges of your graph ("city1","city2").
* Type and enter the command "python3 dotConverter.py"
* Give the program the path to your CSV file with city names and IDs
* Chose if you would like to create a new file named 'desired_cities.csv' that contains the subset of worldcities.csv that you have selected
* Give the program the path to your CSV file with edge information
* Done! you should have the files 'cities.dot' and 'cities.png' in your current working directory

## Acknowledgments

* [README-Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [simplemaps](https://simplemaps.com/data/world-cities)
* [pygraphviz](https://pygraphviz.github.io/)



