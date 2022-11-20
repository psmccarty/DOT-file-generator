#!/usr/bin/env python
# coding: utf-8

#https://simplemaps.com/data/world-cities

from math import radians, cos, sin, asin, sqrt
import csv
import pygraphviz as pgv

# Modified from https://automatetheboringstuff.com/chapter14/
def process_csv(filename):
	"""
	Read data from a csv file.

	Parameters
	----------
	filename : str
		the path of the file to be read.

	Returns
	-------
	list of list of str
		data from CSV file with each row as its own list.
		
	"""

	example_file = open(filename, encoding="utf-8")
	example_reader = csv.reader(example_file)
	example_data = list(example_reader)
	example_file.close()
	return example_data


# sourced from https://www.geeksforgeeks.org/program-distance-two-points-earth/#:~:text=For%20this%20divide%20the%20values,is%20the%20radius%20of%20Earth.
def distance(lat1, lat2, lon1, lon2):
	"""
	Calculate distance between two locations on Earth.

	Parameters
	----------
	lat1 : int or float 
		Latitude of location 1.
	lat2 : int or float
		Latitude of location 2.
	lon1 : int or float
		Longitude of location 1.
	lon2 : int or float
		Longitude of location 2.

	Returns
	-------
	float	
		Distance in KM of the two locations.
		
	"""
    # The math module contains a function named
    # radians which converts from degrees to radians.
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
      
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
	c = 2 * asin(sqrt(a))
    
	# Radius of earth in kilometers. Use 3956 for miles
	r = 6371
      
    # calculate the result
	return(c * r)


# add a node to the graph given two nodes
def addEdgeToGraph(node1, node2, dist):
	"""
	Add undirected edge between two nodes to graph using pygraphviz.

	Edge weight is the distance between the two nodes.

	Parameters
	----------
	node1 : str
		First node in edge.
	node2 : str
		Second node in edge.
	dist : int or float
		Distance in KM between node1 and node2.
	"""
	G.add_edge(node1, node2, weight=dist)
	edge = G.get_edge(node1, node2)
	edge.attr['label'] = edge.attr['weight']



# Use process_csv to pull out the header and data rows
csv_rows = process_csv("worldcities.csv")
csv_header = csv_rows[0] # A list of the column headers
csv_data = csv_rows[1:] # The entire CSV data set besides the headers


# find the idexeces of approriate columns
cityNameIdx = csv_header.index("city_ascii")
latIdx = csv_header.index("lat")
lonIdx = csv_header.index("lng")
idIdx = csv_header.index("id")


#select only the desired cities
inp = input("What is the filepath of the cities and their id's? ")
desired_cities = process_csv(inp)
desired_header = desired_cities[0]
desired_data = desired_cities[1:]


d_cityNameIdx = desired_header.index("city_ascii")
d_idIdx = desired_header.index("id")
#desired_cities = process_csv("cityAndId.csv")


# retreive only the ideces
city_names = []
city_ids = []
for i in range(len(desired_data)):
	city_names.append(desired_data[i][d_cityNameIdx].lower())
	city_ids.append(int(desired_data[i][d_idIdx]))


# select only the rows of data whose id match what the user selected
selected_rows = [] # rows selected from 'worldcities.csv'
coord_dict = {}
for i in range(len(csv_data)):
	if int(csv_data[i][idIdx]) in city_ids:
		selected_rows.append(csv_data[i])
		coord_dict[csv_data[i][cityNameIdx].lower()] = (csv_data[i][latIdx], csv_data[i][lonIdx])

		
# write selected rows to a file
inp = input("Would you like to write the subset of worldcities.csv to a file?(y/n) ").strip()
if(inp.lower() == "y" or inp.lower() == "yes"):
	with open('desired_cities.csv', 'w', newline='', encoding='utf-8') as file:
		writer = csv.writer(file);
		writer.writerow(csv_header);
		writer.writerows(selected_rows);
	print("Wrote subset of world cities to \'desired_cities.csv\'")
	file.close()


# get filepath of edges from user
edges = input("What is the filepath of the desired edges? ")
desired_edges = process_csv(edges)
#desired_edges = process_csv("edges.csv")


# create graph
G = pgv.AGraph()
G.add_nodes_from(city_names)


# add edges to graph
for i in range(len(desired_edges)):
	city1 = desired_edges[i][0].lower().strip().replace('\"', '')
	city2 = desired_edges[i][1].lower().strip().replace('\"', '')

	lat1 = float(coord_dict[city1][0])
	lat2 = float(coord_dict[city2][0])
	
	lon1 = float(coord_dict[city1][1])
	lon2 = float(coord_dict[city2][1])

	d = round(distance(lat1, lat2, lon1, lon2))
	
	addEdgeToGraph(city1, city2, d)
	

G.write("cities.dot")
print("Wrote graph to \'cities.dot\'")
G.layout(prog="dot")
G.draw("cities.png")
print("Drew graph to \'cities.png\'")








