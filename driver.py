from plotter import plotTimesTable, plotTimesTableSequence
import json

if __name__ == "__main__":
    factors = list(range(0,50))
    divisor = 0
    configFileName = "config.json"
    with open(configFileName) as f:
        d = json.load(f)
        divisor = int(d["divisor"])


    plotTimesTableSequence(factors, divisor)