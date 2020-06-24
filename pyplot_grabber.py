import matplotlib.pyplot as plt
import argparse
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='bruh.txt')
parser.add_argument('--title', type=str, default='graph1')
parser.add_argument('--xname', type=str, default='time')
parser.add_argument('--yname', type=str, default='value')

LABEL = "Trial"
args = parser.parse_args()
x = 0

def plot_data(plot):
    ranks = [line.split("|")[0] for line in plot]
    times = [float(line.split("|")[2])/3600 for line in plot]
    accuracies = [float(line.split("|")[3]) for line in plot]
    epochs = [int(line.split("|")[1]) for line in plot]
    print(accuracies)
    if ranks[0] == 0:
        plt.plot(times, accuracies, label="Server Node accuracy", marker = "o") 
    plt.plot(times, accuracies, label="{} {}".format(LABEL, int(ranks[0])), marker = "o" )

with open(args.file) as f:
    lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines] 
    plot = []
    for line in lines:
        if("break" in line):
            plot_data(plot)
            plot.clear()
        else:
            plot.append(line)
plt.ylabel(args.yname)
plt.xlabel(args.xname)
plt.title(args.title)
plt.legend()

plt.tight_layout()
plt.show()