import math
import sys
#Returns the nearest neighbor approximation
def runNearestNeighbor(data):
    index = 0
    unvisited = data.copy()
    visited = []
    current = data[0]
    for i in range(len(data)):
        unvisited.remove(current)
        visited.append(current)
        nextPoint = ()
        minDistance = sys.maxsize
        for candidate in unvisited:
            tempDistance = math.hypot(candidate[0]-current[0],candidate[1]-current[1])
            if tempDistance < minDistance:
                nextPoint = candidate
                minDistance = tempDistance
        current = nextPoint
    return visited
