__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 9
FILENAME : escape.py
Author: Some code from search algorithms lecture code
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program builds a graph and connects the edges. It also
coputes the length taken by the point to escape the grid.
It also prints the final result in the form of a dictionary.
"""

from vertex import Vertex
from graph import Graph
import sys

def insertInDictionary(dict,currentPoint,escapeLength):
    """
    This function prints the final result by inserting the
    result in a dictionary. The result is printed in x y form.

    :param escapeLength: length taken by point to escape
    :param currentPoint: current vertex object or the current point
    """
    if escapeLength in dict:
        newList=dict.get(escapeLength)
        newList.append(currentPoint)
    else:
        pointList=[]
        pointList.append(currentPoint)
        dict[escapeLength]=pointList

def iterateThroughGraph(mList,iceMaze,width,height,row):
    """
    This function iterates through the graph and helps in
    printing the final result
    :param mList: list containing the grid
    :param iceMaze: contains the vertices
    :param width: width of the grid
    :param height: height of the grid
    :param row: row of the grid
    """
    dict={}
    dict1={}
    escapePoint = iceMaze.getVertex((int(row), width - 1))
    for i in range(0,width):
        for j in range(0,height):
            if mList[i][j]!='*':
                currentPoint=iceMaze.getVertex((i,j))
                if findShortestPath(currentPoint,escapePoint)==None:
                    insertInDictionary(dict1,currentPoint.id,'No Path')
                else:
                    escapeLength=len(findShortestPath(currentPoint,escapePoint))-1
                    insertInDictionary(dict,currentPoint.id,escapeLength)

            else:
                continue
    print()
    print("The final result in x y form is : ")
    print()
    for item in dict:
        print(item,":",dict[item])
    print()
    for item in dict1:
        print(item, ":", dict1[item])

def findShortestPath(start, end):
    """
    Find the shortest path, if one exists, between a start and end vertex
    :param start (Vertex): the start vertex
    :param end (Vertex): the destination vertex
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """
    # Using a queue as the dispenser type will result in a breadth first
    # search
    queue = []
    queue.append(start)  # prime the queue with the start vertex

    # The predecessor dictionary maps the current Vertex object to its
    # immediate predecessor.  This collection serves as both a visited
    # construct, as well as a way to find the path
    predecessors = {}
    predecessors[start] = None  # add the start vertex with no predecessor

    # Loop until either the queue is empty, or the end vertex is encountered

    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getConnections():
            if neighbor not in predecessors:  # if neighbor unvisited
                predecessors[neighbor] = current  # map neighbor to current
                queue.append(neighbor)  # enqueue the neighbor

    # If the end vertex is in predecessors a path was found
    if end in predecessors:
        path = []
        current = end
        while current != start:  # loop backwards from end to start
            path.insert(0, current)  # prepend current to the path list
            current = predecessors[current]  # move to the predecessor
        path.insert(0, start)
        return path
    else:
        return None


def isAWall(i,j,mList):
    """
    Checks whether a given point is a wall
    :param i: x coordinate
    :param j: y coordinate
    :param mList: list containing the grid
    :return: boolean value whether the point is a wall or not
    """
    if mList[i][j]=='*':
        return "true"
    else:
        return "false"

def isEdgeJ(i,j,height,width):
    """
    Checks whether point on the y axis is a wall or not
    :param i: x coordinate
    :param j: y coordinate
    :param height: height of the grid
    :param width: width of the grid
    :return: boolean value whether the point is the last point or edge or not
    """
    if j==height-1 or j == 0:
        return "true"
    else:
        return "false"

def isEdgeI(i,j,height,width):
    """
    Checks whether point on the y axis is a wall or not
    :param i: x coordinate
    :param j: y coordinate
    :param height: height of the grid
    :param width: width of the grid
    :return: boolean value whether the point is the last point or edge or not
    """
    if i == width-1 or i == 0:
        return "true"
    else:
        return "false"

def addNeighbours(iceMaze,mList,width,height):
    """
    This is the function which adds neighbours to the graph
    traversing the vertices till the rock. The vertex before the
    rock is considered as the neighbour. The points are traversed
    and the point before the rock is taken as the neighbour of the vertex
    in this graph.
    :param iceMaze: object of the class graph which adds the vertex
    :param mList: list containing the grid
    :param width: width of the grid
    :param height: height of the grid
    :return: the object of the vertex
    """
    for i in range(width):
        for j in range(height):
                currentVertex = iceMaze.getVertex((i, j))
                if isAWall(i,j,mList)=="true":
                    continue
                col = j
                while col<height-1:
                    if mList[i][col+1]=='*':
                        currentVertex.addNeighbor(iceMaze.getVertex((i,col)))
                        iceMaze.addEdge(currentVertex,iceMaze.getVertex((i,col)))
                        break

                    elif isEdgeJ(i,col+1,height,width)=="true":
                        currentVertex.addNeighbor(iceMaze.getVertex((i, col+1)))
                        iceMaze.addEdge(currentVertex,iceMaze.getVertex(((i, col+1))))
                        break
                    else:
                        col=col+1

                col = j
                while col>0:
                    if mList[i][col-1]=='*':
                        currentVertex.addNeighbor(iceMaze.getVertex((i,col)))
                        iceMaze.addEdge(currentVertex, iceMaze.getVertex((i, col)))
                        break

                    elif isEdgeJ(i,col-1,height,width)=="true":
                        currentVertex.addNeighbor(iceMaze.getVertex((i, col-1)))
                        iceMaze.addEdge(currentVertex, iceMaze.getVertex((i, col-1)))
                        break
                    else:
                        col=col-1

                row = i
                while row<width-1:
                    if mList[row + 1][j]=='*':
                        currentVertex.addNeighbor(iceMaze.getVertex((row,j)))
                        iceMaze.addEdge(currentVertex, iceMaze.getVertex((row, j)))
                        break

                    elif isEdgeI(row+1,j,height,width)=="true":
                        currentVertex.addNeighbor(iceMaze.getVertex((row+1, j)))
                        iceMaze.addEdge(currentVertex, iceMaze.getVertex((row+1, j)))
                        break
                    else:
                        row = row + 1

                row = i
                while row >0:
                    if mList[row-1][j]=='*':
                        currentVertex.addNeighbor(iceMaze.getVertex((row,j)))
                        iceMaze.addEdge(currentVertex, iceMaze.getVertex((row, j)))
                        break

                    elif isEdgeI(row-1,j,height,width)=="true":
                        currentVertex.addNeighbor(iceMaze.getVertex((row-1, j)))
                        iceMaze.addEdge(currentVertex, iceMaze.getVertex((row-1, j)))
                        break
                    else:
                        row = row - 1
                print(currentVertex)

def createVertex(mList,height,width,row):
    """
    This function creates the vertex in the graph and also calls the function addNeighbours
    to add the neighbours in the graph
    :param mList: list containing the grid
    :param height: height of the grid
    :param width:  width of the grid
    """
    iceMaze=Graph()
    for i in range(0,width):
          for j in range(0,height):
              iceMaze.addVertex((i,j))

    addNeighbours(iceMaze,mList,width,height)
    iterateThroughGraph(mList,iceMaze,width,height,row)


def readDetails(f1):
    """
    This function reads the files and calls the create vertex function to
    create the vertex
    :param f1: file pointer of file1
    """
    mList=[]
    details=[]
    details=f1.readline().strip("").split(" ")
    for f1_line in f1.read().splitlines():
        mList.append(list(f1_line))
    height=details[0]
    width=details[1]
    row=details[2]
    createVertex(mList,int(height),int(width),row)

def main():
    """
    This is the main function which takes in the file and processes it.
    It also calls the other functions.
    """
    filename = input("enter the file name")
    try:
        fname1=filename
        f1= open(fname1)
        readDetails(f1)
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

if __name__ == '__main__':
 main()