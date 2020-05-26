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

    plt.figure()
    plt.axis('off')
    for i in range(len(x1)):
        plt.plot([x1[i],x2[i]], [y1[i], y2[i]], marker = '', color='#87CEFA',  linewidth=0.25)
        
    plt.savefig("timesTable-f" + str(factor) + "-d" + str(divisor) +".png", bbox_inches='tight',  dpi=300)

def plotTimesTableSequence(factors, divisor):
    for factor in factors:
        plotTimesTable(factor, divisor)