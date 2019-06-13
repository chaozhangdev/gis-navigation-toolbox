import arcpy
import math
import re

from arcpy import env
from collections import defaultdict

env.overwriteOutput = True
env.workspace = "C:/Users/CHAO/Desktop/GIS Project_Chao Zhang/city of vancouver.gdb"

#units = arcpy.Describe("park_polygons").spatialReference.linearUnitName
units = "meters"

input_id = arcpy.GetParameter(0)
input_type = arcpy.GetParameter(1)

# calculation of the distance
def dis(a,b):
	result = math.sqrt(a*a + b*b)
	return result


def getposition_citizen(id_num):
	fc = "property_addresses"
	cursor = arcpy.da.SearchCursor(fc,["SHAPE@XY","OID@"])
	for row in cursor:
		if row[1] == id_num:
			x,y = row[0]
	del row
	del cursor
	return x,y


def destination_info(type):
	if type == "park":
		return ("park_polygons","PARK_NAME")
	if type == "library":
		return ("libraries","NAME")
	if type == "school":
		return ("schools","NAME")


def location_distance_calc(c_x,c_y,fc,a_name):
	cursor = arcpy.da.SearchCursor(fc,["SHAPE@XY",a_name])
	s = 99**9 #99^9 is 913517247483640899 which is large enough for the initialization of value of s
	for row in cursor:
		x,y = row[0]
		distance = dis(x-c_x,y-c_y)
		if distance<s:
			s = distance
			name = row[1]
			l_x = x
			l_y = y
	del row
	del cursor
	return name,l_x,l_y


def store_street_intersections():

	data = []
	for i in xrange(6970):
		data.append([])
		for j in xrange(3):
			data[i].append([])

	fc = "street_intersections"
	cursor = arcpy.da.SearchCursor(fc,["OID@","SHAPE@XY","XSTREET"])

	for row in cursor:	
		num = row[0]
		x,y = row[1]
		data[num][0] = num
		data[num][1] = x
		data[num][2] = y

	del row
	del cursor

	return data


def get_max_and_min(x,y,park_x,park_y):

	if x>park_x:
		max_x = x
		min_x = park_x
	else:
		max_x = park_x
		min_x = x
	if y>park_y:
		max_y = y
		min_y = park_y
	else:
		max_y = park_y
		min_y = y
	return min_x,max_x,min_y,max_y


def get_region(start_x,end_x,start_y,end_y,storedata):  #select conjunctions

	data = []
	t = 0
	for i in xrange(6970):
		x = storedata[i][1]
		y = storedata[i][2]
		if x>start_x and x<end_x and y>start_y and y<end_y:
			data.append([])
			for j in xrange(3):
				data[t].append([])
			data[t][0] = i
			data[t][1] = x
			data[t][2] = y
			t+=1

	return data,t


def get_street(start_x,end_x,start_y,end_y,storedata):

	data = []
	t = 0
	fc = "public_streets"
	cursor = arcpy.da.SearchCursor(fc,["SHAPE@","SHAPE@XY","HBLOCK"])

	for row in cursor:
		x,y = row[1]
		if x>start_x and x<end_x and y>start_y and y<end_y:
			s = 0
			data.append([])
			data[t].append([])
			data[t][s] = row[2]
			s+=1
			for point in row[0].getPart(0):
				data[t].append([])
				data[t][s] = point.X,point.Y
				s+=1
			t+=1

	for i in xrange(len(data)-1):
		for j in xrange(i+1,len(data)):
			if data[i][0] == data[j][0]:
				add = data[j][1:len(data[j])]
				for k in xrange(len(add)):
					data[i].append(add[k])
				data[j][0] = "del"	

	newdata = []

	for list in data:
		if list[0] != "del":
			newdata.append(list)

	return newdata,len(newdata)


def create_gragh(region,region_num,street):

	data = []
	t = 0
	for i in xrange(region_num-1):
		for j in xrange(i+1,region_num):
			for list in street:
				if (region[i][1],region[i][2]) in list and (region[j][1],region[j][2]) in list:
					data.append([])
					for k in xrange(3):
						data[t].append([])			
					data[t][0] = region[i][0]
					data[t][1] = region[j][0]
					data[t][2] = dis (region[i][1]-region[j][1],region[i][2]-region[j][2])
					t+=1
	return data


#dijsktra

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {} 
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()   
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


def shortest(region,x,y,l_x,l_y):

	start = 99**9 
	end = 99**9
	for list in region:
		num = list[0]
		xxx = list[1]
		yyy = list[2]
		if dis(x-xxx,y-yyy)<start:
			start = dis(x-xxx,y-yyy)
			start_num = num
		if dis(xxx-l_x,yyy-l_y)<end:
			end = dis(xxx-l_x,yyy-l_y)
			end_num = num

	return start_num,end_num


def navigation(path,region,street,type,l_name):

	arcpy.AddMessage ("The nearest {0} near your address is: {1}".format(type,l_name))

	arcpy.AddMessage ("Route calculation:")

	origin = []
	draw = []
	for count in xrange(len(path)-1):
		num1 = path[count]
		num2 = path[count+1]
		for list in region:
			if list[0] == num1:
				x1 = list[1]
				y1 = list[2]
			if list[0] == num2:
				x2 = list[1]
				y2 = list[2]

		for list in street:
			if (x1,y1) in list and (x2,y2) in list:
				mark = list[0]
				distance = int(round(dis (x1-x2,y1-y2)))	
				pointA = (x1,y1)
				draw.append(pointA)
				pointB = (x2,y2)
				draw.append(pointB)

		turn = re.split(' ',mark)
		turn.pop(0)

		if count == 0:
			origin = turn

		if turn != origin:
			arcpy.AddMessage ("Make a trun at the intersection")
			origin = turn

		arcpy.AddMessage ("Go striaght along {0}: {1} {2}s".format(mark,distance,units))

	arcpy.AddMessage ("You have reached your destination, have a nice day!")
	
	#draw the output
	newfc = "navigation_output"
	cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
	array = arcpy.Array()
	for data in draw:
		x,y = data
		array.add(arcpy.Point(x,y))
	cursor.insertRow([arcpy.Polyline(array)])
	del cursor



citizenID =  input_id       
destination_type = input_type       

filename,attribute_name = destination_info(destination_type)
p_x,p_y = getposition_citizen(citizenID)

location_name,l_x,l_y = location_distance_calc(p_x,p_y,filename,attribute_name)
min_x,max_x,min_y,max_y = get_max_and_min(p_x,p_y,l_x,l_y)

storedata = store_street_intersections()
region,region_num = get_region(min_x-600,max_x+600,min_y-600,max_y+600,storedata)
street,street_num = get_street(min_x-600,max_x+600,min_y-600,max_y+600,storedata) 

edges = create_gragh(region,region_num,street)
graph = Graph()
for edge in edges:
    graph.add_edge(*edge)

start,end = shortest(region,p_x,p_y,l_x,l_y)
path = dijsktra(graph,start,end)

navigation(path,region,street,destination_type,location_name)
