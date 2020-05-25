from utilities import computeModulusTimesTable, findClockPositions
import matplotlib.pyplot as plt
import numpy as np

def plotTimesTable(factor, divisor):
    first = np.array(range(0, divisor)).astype(float)
    second = computeModulusTimesTable(first, factor, divisor)
    
    positions = findClockPositions(
        first,
        second,
        divisor)

    x1 = positions["x1"]
    x2 = positions["x2"]
    y1 = positions["y1"]
    y2 = positions["y2"]

    for i in range(len(x1)):
        plt.plot([x1[i],x2[i]], [y1[i], y2[i]], marker = 'o', color='blue')
    plt.savefig("timesTable-f" + str(factor) + "-d" + str(divisor) +".png")

def plotTimesTableSequence(factors, divisor):
    for factor in factors:
        plotTimesTable(factor, divisor)