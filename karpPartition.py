import branchAndBound
import math
#Runs the Karp Partition algorithm on the given set of points
def runKarpPartition(data):
    k = calculateK(len(data),4) #we can change the t, here it is 4
    (spanWalk, midpoints) = walk(data, k)
    spanWalk.reverse()
    for point in midpoints:
        spanWalk.remove(point) #if two points are in different partitions, we know they dont form a cut set. Therefore this is performing pass
    return spanWalk

#sorts a list of points by X value
def sortByX(point):
    return point[0]
#sorts a list of points by X value
def sortByY(point):
    return point[1]

#calculates our k value given the number of points and the size of 
#tour after which we call an optimal solution
def calculateK(n,t):
    return math.ceil(math.log((n-1)/(t-1),2))

#Returns the left and right partitions of a set of points as a tuple
def split(points):
    maxX = points[0][0]
    minX = points[0][0]
    maxY = points[0][1]
    minY = points[0][1]
    for point in points:
        if point[0] > maxX:
            maxX = point[0]
        if point[0] < minX:
            minX = point[0]
        if point[1] > maxY:
            maxY = point[1]
        if point[1] < minY:
            minY = point[1]
    #determines we should split it by x or y
    if maxX - minX > maxY - minY:
        points.sort(key = sortByX)
    else:
        points.sort(key = sortByY)
    midpoint = math.ceil((len(points))/2)
    left = []
    right = []
    for i in range(len(points)):
        if i <= midpoint:
            left.append(points[i])
        if i >= midpoint:
            right.append(points[i])
    return (left,right, points[midpoint])

#Finds a spanning walk, returns it as a list of points
def walk(data, j):
    if j == 0:
        return (branchAndBound.runBranchAndBound(data),[])
    (left, right, midpoint) = split(data)
    (left,leftMidpoints) = walk(left, j-1)
    (right,rightMidpoints) = walk(right, j-1)
    while left[0] != midpoint: #this will make sure our deconstructing works
        rotate(left)
    while right[0] != midpoint:
        rotate(right)
    midpoints = leftMidpoints+rightMidpoints
    midpoints.append(midpoint)
    return (left + right, midpoints)

#rotating the list leftward
def rotate(points):
    points.append(points.pop(0))
