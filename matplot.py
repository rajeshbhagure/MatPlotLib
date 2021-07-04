import matplotlib.pyplot as plt
import numpy as np
import sys


def pyplot():
    xpoints = np.array([0, 6,12,18])
    ypoints = np.array([0, 250,300,40])
    plt.plot(xpoints, ypoints,marker='o')
    plt.show()
pyplot()


def line():
    ypoints = np.array([3, 8, 1, 10])
    xpoints = np.array([5, 10, 15, 12])

    plt.plot(ypoints,xpoints,linestyle='dashed')
    plt.show()
line()



def subplots():
    # plot 1:
    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(1, 2, 1)
    plt.plot(x, y)

    # plot 2:
    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 25])

    plt.subplot(1, 2, 2)
    plt.plot(x, y)

    plt.show()

subplots()



def scatter():
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    plt.scatter(x, y, color='hotpink')

    x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
    y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
    plt.scatter(x, y, color='#88c999')

    plt.show()
scatter()



def bar():
    x = np.array(["A", "B", "C", "D"])
    y = np.array([3, 8, 1, 10])

    plt.bar(x, y, color="pink")
    plt.show()
    
bar()


def piechart():
    y = np.array([35, 25, 25, 45])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    plt.pie(y, labels=mylabels)
    plt.show()

    # Two  lines to make our compiler able to draw:

    # plt.savefig(sys.stdout.buffer)
    # sys.stdout.flush()
    
piechart()
