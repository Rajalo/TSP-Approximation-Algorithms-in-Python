#This file implements Christofedes' algorithm
import kruskal
from collections import deque as stack
import math
import networkx as nx
import time

#runs the original christofedes algorithm
def runChristofedes(data):
    mstPoints = kruskal.mstFull(data) #min spanning tree
    oddDegree = []
    for point in mstPoints:
        if len(point.neighbors) %2 == 1:
            oddDegree.append(point)
    matchingEdges = perfectMatching(oddDegree) #adds in min cost perfect matching
    for edge in matchingEdges: #manually adds in edges from the matching
        edge[1].neighbors.append(edge[0])
        edge[0].neighbors.append(edge[1])
    eulerList = eulerCircuit(mstPoints) #finds an euler circuit of the given edges
    return hamiltonizeCircuit(eulerList) #converts that euler circuit into a hamiltonian one

#finds a pefect matching for the given data set, returns as a list of edges
def perfectMatching(data):
    edgesComplete = []
    for i in range(len(data)):
        if i == 0:
            continue
        for j in range(i):
            weight = -edgeWeight((data[j].coords,data[i].coords))
            edgesComplete.append((data[j],data[i],{'weight': weight}))
    graph = nx.Graph()
    graph.add_edges_from(edgesComplete)
    matching = nx.algorithms.max_weight_matching(graph,maxcardinality=True)
    return list(matching)

def edgeWeight(edge):
    return math.hypot(edge[0][0]-edge[1][0],edge[0][1]-edge[1][1])

#returns a euler circuit using Hierholzer's algorithm, returns as a list of points
def eulerCircuit(vertices):
    n = len(vertices)
    degrees = [0]*n
    i = 0
    for point in vertices:
        if len(point.neighbors) %2 == 1: #checking that everything has even degree for the circuit to work
            return []
        degrees[i] = len(point.neighbors)
        i += 1
    tempPath = stack()
    finalPath = []
    currentVertex = vertices[0]
    tempPath.append(currentVertex)
    while tempPath:
        currentVertex = tempPath[-1]
        if not currentVertex.neighbors:
            tempPath.pop()
            finalPath.append(currentVertex.coords)
        else:
            tempVertex = currentVertex.neighbors[0]
            currentVertex.removeNeighbor(tempVertex)
            tempVertex.removeNeighbor(currentVertex)
            tempPath.append(tempVertex)
    return finalPath

def hamiltonizeCircuit(nodesList):
    newList = []
    for node in nodesList:
        if not node in newList:
            newList.append(node)
    return newList

if __name__ == "__main__":
    coords = [(1,1),(2,2),(3,0),(0,2)]
    points = []
    for coord in coords:
        points.append(kruskal.Point(coord))
    print(runChristofedes(coords))