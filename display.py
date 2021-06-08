#This file is used to display the results of various algorithms
import matplotlib.pyplot as plt
import numpy
import christofedes
import nearestNeighbor
import insertion
import branchAndBound
import karpPartition

#Shows the various paths which each algorithm chose to approximate the optimal
#Works best when mapping one or two algorithms but extensible to any number
def plotTours(data, *methods):
    plt.figure("Approximation Tours")
    for method in methods:
        order = method(data)
        order.append(order[0])
        name = methodToString(method)
        plt.plot(*zip(*order), label = name)
    plt.plot(*zip(*data), 'o')
    plt.title("Approximation Tours for the given points")
    plt.legend(loc = "best")
    plt.show()

#Converts the method's string representation to something readable for display
def methodToString(method):
    string = str(method)
    startIndex = string.index("run")+3
    endIndex = string.index(" ", startIndex)
    return string[startIndex:endIndex]

#Generates the given number of random points
def generateRandomPoints(size):
    return [(numpy.random.uniform(0.0,10.0),numpy.random.uniform(0.0,10.0)) for i in range(size)]


if __name__ == "__main__":
    plotTours(generateRandomPoints(20), karpPartition.runKarp)