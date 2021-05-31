# Contains various insertion-type algorithms for finding the TSP tour

import random
import sys
import math

#Simply selects a random node from the unvisited nodes
#Returns a -1 to indicate the need to find the insertion index
def selectRandom(current, remaining):
    if len(remaining)<=1:
        return (remaining[0],-1)
    return (remaining[random.randint(0,len(remaining)-1)],-1)

#Selects the nearest unvisited node to the visited nodes
#Returns the insertion index
def selectNearest(current, remaining):
    newNode = remaining[0]
    minDistance = sys.maxsize
    for candidate in remaining:
        for node in current:
            temp  = dist(candidate,node) 
            if temp < minDistance:
                minDistance = temp
                newNode = candidate
    return (newNode,-1)

#Selects the furthest unvisited node from the visited nodes
#Returns a -1 to indicate the need to find the insertion index
def selectFarthest(current, remaining):
    newNode = remaining[0]
    maxDistance = 0
    for candidate in remaining:
        for node in current:
            temp  = dist(candidate,node) 
            if temp > maxDistance:
                maxDistance = temp
                newNode = candidate
    return (newNode,-1)

#Selects the cheapest unvisited node to insert
#Returns a -1 to indicate the need to find the insertion index
def selectCheapest(current,remaining):
    newNode = remaining[0]
    index = 0
    minCost = sys.maxsize
    for candidate in remaining:
        for i in range(len(current)):
            u = current[i]
            v = current[(i+1)%len(current)]
            temp = cost(u,candidate,v)
            if temp < minCost:
                minCost = temp
                newNode = candidate
                index = i
    return (newNode,index)

#adds a node into the current
def addNode(current, remaining, selectionMethod):
    (newNode,index) = selectionMethod(current,remaining)
    if index == -1:
        index = 0
        length = sys.maxsize
        for i in range(len(current)):
            u = current[i]
            v = current[(i+1)%len(current)]
            temp = cost(u,newNode,v)
            if temp < length:
                length = temp
                index = i
    current.insert(index+1, newNode)
    remaining.remove(newNode)
    return (current, remaining)

#runs the insertion algorithm given a selection method
def runInsert(data, selectionMethod):
    current = [data[0]]
    remaining = data.copy()
    remaining.remove(data[0])
    #for i in range(3):
    for i in range(len(data)-1):
        addNode(current, remaining, selectionMethod)
    return current

#runs the random insertion algorithm on a given set of points
def runRandomInsertion(data):
    return runInsert(data,selectRandom)

#runs the nearest insertion algorithm on a given set of points    
def runNearestInsertion(data):
    return runInsert(data,selectNearest)

#runs the farthest insertion algorithm on a given set of points    
def runFarthestInsertion(data):
    return runInsert(data,selectFarthest)

#runs the cheapest insertion algorithm on a given set of points    
def runCheapestInsertion(data):
    return runInsert(data,selectCheapest)

#calculates 2D Euclidean distance
def dist(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])
#calculates the cost of incorporating edges (a,b),(b,c)
def cost(a,b,c):
    return dist(a,b)+dist(b,c)-dist(a,c)