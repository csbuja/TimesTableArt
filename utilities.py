import numpy as np

def computeModulusTimesTable(x, factor, divisor):
    return np.mod(x * factor, divisor)


def findClockPositions(first, second, divisor: int):
    R = 1.0
    convertToRadiansFactor = np.pi * 2 / divisor

    x1 = R * np.cos(first * convertToRadiansFactor)
    y1 = R * np.sin(first * convertToRadiansFactor)
    x2 = R * np.cos(second * convertToRadiansFactor)
    y2 = R * np.sin(second * convertToRadiansFactor)

    return {
        "x1":x1,
        "x2":x2,
        "y1":y1,
        "y2":y2
    }

if __name__ == "__main__":
    # test computeModulusTimesTable 1
    vals = computeModulusTimesTable(np.array([0,1,2,3,4]), 2, 5)
    expecteds = np.array([0, 2, 4, 1, 3])
    for output,expected in zip(vals,expecteds):
        assert(output == expected)


    # test findClockPositions 1
    first = np.array([0,2])
    second = np.array([1,3])
    divisor = 4
    d = findClockPositions(first, second, divisor)

    expectedX1 = [1,-1]
    expectedX2 = [0, 0]
    expectedY1 = [0, 0]
    expectedY2 = [1,-1]
    

    expecteds = expectedX1 + expectedX2 + expectedY1 + expectedY2
    outputs = list(d["x1"]) + list(d["x2"]) + list(d["y1"]) + list(d["y2"])
    outputs = np.round(outputs)

    for output,expected in zip(outputs,expecteds):
        print("output " + str(output))
        print("expected " + str(expected))
        assert(output == expected)
    
