# GIS - City of Vancouver Navigation Toolbox Development

## Abstract
As the demand for navigation access increases so does the improvement of
software development, more and more navigation tools have been created for efficient
life among cities. This project is to create a new navigation toolbox based on ArcGIS by python
scripts to provide users shortest route information among two arbitrary places among
the city of Vancouver. The input are citizens addresses ID or names of different places with their types
and results can offer users detailed navigation including street names, travelling
distances and positions of street intersections.
*Key word: navigation; shortest route; Dijskra’s algorithm.*

## 1.0 Introduction
Nowadays, navigation plays a more and more significant role in urban city life
especially in some big cities. It has totally replaced traditional maps for users to find a
location or select an optimal route among cities in our daily life.
In this project, a navigation toolbox has been created containing four functions in
city of Vancouver based on geographic information system(GIS). Users can use this
toolbox to easily find nearest or specified school, library or school from home among
Vancouver, get shortest a route between two properties and obtain a shortest path
between two given different places. It will show users detailed information in
navigation which contains street names, street lengths and positions of intersections.
The motivation of undertaking the research is from daily life. Every time when I
use Google map, I notice it is an essential software among people and wonder if there
is possible to make a navigation software like that by myself.
GIS provides XY coordinates and some attributes of every object in Vancouver,
relationships among different objects can be found and spatial positions with
geographic references are reliable to analyze to create new toolbox. The general
solution for navigation in this project is to locate start and end points first, then choose
network area covering these two points and last analyze this network area to provide
an optimal path. In the rest of this report, it will illustrate data collection, flowchart of
solution, details in network area analysis which is how to find an optimal path and
Dijsktra’s algorithm applied in shortest route calculation.

## 2.0 Literature Review
In this section of report, it provides previous research with new ideas and changes
to current research, core algorithm used in project, how algorithm be applied into
project and algorithm improvements.

## 2.1 Previous Work Review
In previous work, UNA toolbox from MIT City Form Lab is used to solve the
shortest route problem and it can get the shortest path easily just by input start and end
data. However, a new idea came to my mind is to create a navigation toolbox by
myself which can calculate the shortest path among the whole Vancouver city network
based on Dijkstra’s algorithm.

## 2.2 General steps of Dijkstra’s Algorithm
Dijkstra’s algorithm is an advanced version of greedy algorithm for finding the
shortest path between nodes in a graph. Dijkstra, E. W. (1959) first found there was an
approach to construct the tree of minimum total length between the n nodes and find
the path of minimum total length between two given nodes to get a shortest path. The
general steps of this approach can be concluded in six step: 1. Mark all unvisited
nodes and create a set containing all unvisited nodes. 2. Set initial node value 0 as
current node and assign every node a tentative distance value. 3. Calculate the
distance between current node and all its neighbour nodes to get the shortest tentative
distance and mark it. 4. Once checking all neighbour nodes of current node, mark
current node which we have visited and remove it from the set we generated in step
one. 5. When the shortest tentative distance is infinity or it has come to the final
unvisited node, Dijkstra’s algorithm has finished. 6. If it does not come to the end,
select the unvisited node with shortest distance as current node and go back to step
three.

## 2.3 Similarities and Differences with Approaches
For similarities, Dijkstra’s algorithm provides a mathematical solution for finding
a shortest path among a weighted graph and the project purpose is also to yield a
shortest route among the city network. However, Dijkstra’s algorithm can not be used
directly among city network and there is a model need to be created for application.

## 2.4 Apply Dijkstra’s Algorithm into City Network
Building city network for Dijkstra’s algorithm to use is to create a weighted graph
based on street intersections where street intersections represent for nodes in graph
and different street lengths between two nodes represent for corresponding distances
between two intersections. Due to the large data set consisted of whole intersections
and streets in Vancouver should be processed, there is impossible to store all data and
use Dijkstra’s algorithm to calculate a shortest path among the whole city. What has
been done is to find a particular area covering start and end points and then perform
calculation in this specific area which can save plenty of time and storage space.

## 2.5 Improvement of Dijkstra’s Algorithm
In DongKai Fan and Ping Shi (2010) research, they improved storage structure
and searching area algorithm which are two drawbacks of classical Dijkstra’s
algorithm. Their algorithm appended analysis of space complexity and analysis of
time complexity for storage structure and set restricted search area when finding next
node during route calculation. It is possible to create an advanced version of Dijkstra’s
Algorithm in this project to select searching area in finding network regions among
the city and store processed topological relationships by deleting some unnecessary
intersections.


## 3.0 Study Area Description
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/1.png)
Study area in this project is the city of Vancouver. It contains 17013 public streets,
6092 street intersections, 100851 property addresses, 264 parks, 194 schools and 21
libraries and all of these data mentioned are analyzed in the project. For other data
such as non city streets, lines, city projects sites, traffic signals and so on are added to
consist of the final map but these data are not processed.

## 4.0 Description of Datasets & Data Preprocessing
This section will outline the table listing of input data sets and attributes of data set used in analysis, data collecting, development of geodatabase, data checking and
preprocessing.

## 4.1 Listing Table of Input Data
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/2.png)

## 4.2 Listing Table of Data for Spatial Analysis
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/3.png)


## 4.3 Listing Table of Attributes for Spatial Analysis
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/4.png)

## 4.4 Data Collecting and Geodatabase Development
All data mentioned are downloaded directly from the website established by the
government of Vancouver. Once these data are ready to use, a new layer is created in
ArcMap to project these data. Then a file geodatabase is created to store selected shape files.

## 4.5 Data Checking and Preprocessing
After finishing building map, checking attribute data of these shape files makes
sure data ready to use are reliable. For error and blank in data attribute, the best way is
to find information online then fill and correct them. After checking data attribute, it
shows data are almost good expect for one problem that the designer got some errors
when digitizing public_street shape file. Some of streets are separated in this shape
file which means some streets may contain more than two points(two points refer to
start point and end point consisted of a whole street). As for data preprocessing, it is
necessary to join these separated streets with the same street name into a whole street
then store these street information into one list for next operations. What has been
solved is to store all streets with street name and XY coordinates into a list first, then
process these streets with same street names, join XY coordinates of these streets
having the same street name together to update a new street connecting separated
information and then delete repeating elements.

## 5.0 Methodology
This section covers a flowchart of solution, an introduction to created functions, a
detailed description including seven steps of spatial analysis methods and
explanations of core python scripts.


## 5.1 Flowchart of Solution
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/5.png)
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/6.png)

## 5.2 List of Created Functions
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/7.png)

## 5.3 Detailed Description of Methods
*Step 1: Store street intersections*

Street intersections are consisted of the whole city network so the first thing is to
store intersections attributes from shape file into an array. A function is created and
the python scripts is below:

def store_street_intersections():

data = []

for i in xrange(6970):

data.append([])

for j in xrange(3):

data[i].append([])

fc = "street_intersections.shp"

cursor=arcpy.da.SearchCursor(fc,["FID","SHAPE@XY"])

for row in cursor:

num = row[0]

x,y = row[1]

data[num][0] = num

data[num][1] = x

data[num][2] = y

del row

del cursor

return data

















