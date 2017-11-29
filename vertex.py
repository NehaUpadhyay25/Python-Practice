"""
CSCI-603: Graphs
Author: Sean Strout @ RIT CS

Authors  : Neha Upadhyay  (nxu3128@rit.edu)

An implementation of a vertex as part of a graph.
This is the given class code.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    """

    __slots__ = 'id','connectedTo'

    def __init__(self, key):
        """
        Initialize a vertex
        :param key: key value

        :return: None
        """
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight (int): The edge cost
        :return: None
        """
        self.connectedTo[nbr] = nbr

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        return str(self.id) + ' connectedTo: ' + str([str(x.id) for x in self.connectedTo])

    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight (int)
        """
        return self.connectedTo[nbr]

def testVertex():



    vertexA = Vertex('A')
    vertexB = Vertex('B')
    vertexC = Vertex('C')
    vertexD = Vertex('D')
    vertexA.addNeighbor(vertexB)
    vertexA.addNeighbor(vertexC)
    vertexB.addNeighbor(vertexA)
    vertexB.addNeighbor(vertexC)
    vertexC.addNeighbor(vertexD)

    # test __str__()
    print(vertexA)
    print(vertexD)

    # test getWeight()
    print('A -> B weight (3):', vertexA.getWeight(vertexB))
    print('C -> D weight (5):', vertexC.getWeight(vertexD))

    # test getConnections():
    print("B's neighbors ():", [vertex.id for vertex in vertexB.getConnections()])
    print("D's neighbors ():", list(vertexD.getConnections()))

if __name__ == '__main__':
    testVertex()
