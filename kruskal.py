#Implementation of Kruskal's algorithm for finding the minimum spanning tree
import math
import time

#finds the length of the mst for the given sequence of points in Euclidean Space
def mstLength(sequence):
    edges = edgeList(sequence)
    edges.sort(key = edgeLength)
    disjointSet = DisjointSet(sequence)
    length = 0
    index = 0
    while disjointSet.length > 1 and index < len(edges):
        if (disjointSet.union(edges[index])):
            length += edgeLength(edges[index])
        index += 1     
    return length

def mstFull(sequence):
    points = []
    for node in sequence:
        points.append(Point(node))
    edges = edgeList(points)
    edges.sort(key = edgeLengthPoint)
    disjointSet = DisjointSet(points)
    finalEdges = []
    index = 0
    while disjointSet.length > 1 and index < len(edges):
        if (disjointSet.union(edges[index])):
            finalEdges.append(edges[index])
            edges[index][0].addNeighbor(edges[index][1])
            edges[index][1].addNeighbor(edges[index][0])
        index += 1
    return points


#Point object which makes it easier to figure out what nodes to use
class Point:
    def __init__(self, coords):
        self.coords = coords
        self.neighbors = []
    def addNeighbor(self, point):
        if point in self.neighbors:
            return False
        self.neighbors.append(point)
        return True
    def removeNeighbor(self, point):
        self.neighbors.remove(point)
    def __str__(self):
        string = self.coords.__str__()+" with neighbors: "
        for point in self.neighbors:
            string += str(point.coords) + ","
        return string

#Generates a list of potential edges from a sequence of points
def edgeList(sequence):
    edges = []
    for i in range(len(sequence)):
        if i == 0:
            continue
        for j in range(i):
            edges.append((sequence[j],sequence[i]))
    return edges
#Finds the Euclidean length of an edge
def edgeLength(edge):
    return math.hypot(edge[1][1]-edge[0][1],edge[1][0]-edge[0][0])
def edgeLengthPoint(edge):
    return math.hypot(edge[1].coords[1]-edge[0].coords[1],edge[1].coords[0]-edge[0].coords[0])

#This class holds a list of disjoint sets of vertices
class DisjointSet:
    def __init__(self, sequence):
        self.sets = []
        self.length = len(sequence)
        for point in sequence:
            self.sets.append({point})
    #this performs a union on the sets bridged by the given edge
    #it will return false if such a union would produce a cycle
    #or is otherwise invalid
    def union(self, edge):
        first = {}
        second = {}
        for set in self.sets:
            if edge[0] in set:
                first = set
            if edge[1] in set:
                second = set
        if (first == second or first == {} or second == {}):
            return False
        newset = first.union(second)
        self.sets.remove(first)
        self.sets.remove(second)
        self.sets.append(newset)
        self.length -= 1
        return True

if __name__ == "__main__":
    lst = [(2,0),(-2,0),(1,-1),(1,1),(-1,1),(-1,-1),(0,0)]
    print(lst)
    mst = mstFull(lst)
    for point in mst:
        print(point)
