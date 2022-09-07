import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import seaborn as sns
import pandas as pd
SENSITIVE = 1
RESISTANT = 0
NOPROGRESSION = -1

def HeatMap(data, xticks, yticks, xlabel, ylabel, title):
    ax = plt.gca()
    im = ax.imshow(data)
    ax.set_xticks(np.arange(len(xticks)), labels=xticks)
    ax.set_yticks(np.arange(len(yticks)), labels=yticks)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    for i,_ in enumerate(yticks):
        for j,_ in enumerate(xticks):
            ax.text(j, i, f"{int(data[i, j])}", ha="center", va="center", color="w", size=5)
    ax.set_title(title)


#data extraction
def TTP(populations, progressionpop, startpopulation):
    TOTAL = populations[RESISTANT] + populations[SENSITIVE]
    for day, pop in enumerate(TOTAL):
        if pop > progressionpop:
            for start, pop in enumerate(TOTAL):
                if pop > startpopulation:
                    DRUGSTART = start
                    TIME = day - DRUGSTART
                    return TIME
    return NOPROGRESSION

def GetData(path,density,conc,trial):
    densityStr="{:.2f}".format(density)
    concStr="{:.2f}".format(conc)
    return np.loadtxt(fr"{path}\DrugConcentrationResponse{densityStr}_{concStr}_{trial}.csv",delimiter=",")
