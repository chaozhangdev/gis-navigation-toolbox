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
store intersections attributes from shape file into an array. A three dimensional list called ‘data’ has been created containing three attributes which are feature ID of intersections and their X Y coordinates separately. From the
for loop, the range is 6970 which means there are 6970 intersections in Vancouver and
these intersections information have been stored in list ‘data’. For spatial data analysis,
it is not wise to process all intersections because it may cost a long time. Next section
will illustrate how to select specific region containing few intersections according to
users input data to reduce unnecessary process, the selected region of streets and
details of operations.

*Step 2: Collect necessary spatial data from input*

According to input user address ID, it is efficient to use a search cursor in address
shape file and easily get XY coordinate from FID. A part of property_addresses
attribute table and function are below:

![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/8.png)

Due to the name domain in park is different from other two so we must use ‘if’ to
select feature names. After this process, it can get the nearest place to user address.
For example, if the user want to go to nearest park, for every park in our map, it
contains its own XY coordinate. A part of of park_polygons attribute table is below:

![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/9.png)

Then a search cursor can be used for every single park to calculate the absolute
distance 2
1 2
2
1 2 (x  x )  ( y  y ) between every park (x1,x2) and user’s home (x2,y2)
and then output the nearest one’s XY coordinate and name. For school and library,
there are the same as park. So far, we have start point XY coordinate and destination
XY coordinate with names.

*Step 3: Select region which should be analyzed from the map*
This step is to avoid unnecessary processes because it need not always compute
all intersections and streets data in Vancouver which may causes few minutes even
Topic in GIS & Geoprocessing Final Project Report
15 few hours. Therefore, a selected region should be assigned. For example, there are
start point which is the red triangle and end point which is green rectangle in Figure 3.
The original region is light red rectangle and processed region is dark rectangle after
adding boundary for original region to make sure all intersections which may affect
route calculation are covered. The minimum distance for boundary is 600 meters
which has been tested for this number covering routes between all addresses and
selected places.
![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/10.png)

The next process is to store all intersections in this region into one list and all
streets in this region into another list. Because there already exists a list containing all
6970 intersections in data preprocessing, so this process just need to clip some of
them from the whole intersections data set into a new list.
When it comes to streets storing, it needs some operations to solve maker’s error
in public street shape file. The purpose is to connect separated streets into a whole
street. Function get_street below can both store streets data and process separated
streets connections.

*Step 4: Create graph*
For every intersection in the region, distances between every single intersection
need to be created and then output the graph which is a three-dimensional list
containing one start node, one end node and the distance between them. Function
create_graph can yield the graph by input street intersections and streets in the
selected region.

*Step 5: Use Dijsktra algorithm to output the shortest route*
In this section, scripts are from open source code online and have been some
changes to be adapt to the whole project. In create_gragh function, the return data
fromat has changed to [node1, node2, distance] to match input format in dijsktra algorithm function. The result of this function is a shortest route containing all passing nodes which is a list consisted of different pairs of intersection to intersection.

*Step 6: Print navigation output*
After getting the shortest path, it can print navigation information for users.
Function navigation can show street names, street lengths and intersection positions.
Due to the shortest path output does not contain street names only has
intersections ID, the first two loops are to find XY coordinate of two intersections
according to their ID. Then the next loop is to find the street which contains these two
intersections. Then it can print street name and the distance how long users should go.
In Canada, straight roads are classified into roads with same name without different
numbers in front of them. So parameters ‘turn’ and ‘origin’ in this function are used to
mark if the main street name has changed which means there is no longer straight
road in there and then it can remind users may make a turn at the intersection.

*Step 7: Create toolbox*
Based on this script, there are some changes have been added and the project
finally yields four different tools for users: 1. property addresses navigation which can
provide navigation information from one property address to another address; 2.
shortest route navigation which is from one property address to nearest park, school or
library; 3. specified destination navigation gives users a path from property address to
specific park, school or library; 4. two given places navigation offers a shortest route
from one place to another place among parks, libraries and schools. For various input
data types, four interfaces are different and they are shown below:

![alt text](https://github.com/zzzchaozzz/GIS/blob/master/img/11.png)

