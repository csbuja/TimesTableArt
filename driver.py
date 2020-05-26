from plotter import plotTimesTable, plotTimesTableSequence
import json

if __name__ == "__main__":
    factors = []
    divisor = 0
    configFileName = "config.json"
    with open(configFileName) as f:
        d = json.load(f)
        divisor = int(d["divisor"])
        maxFactor = int(d["maxFactor"])
        minFactor = int(d["minFactor"])
        factors = list(range(minFactor, maxFactor + 1))


    plotTimesTableSequence(factors, divisor)