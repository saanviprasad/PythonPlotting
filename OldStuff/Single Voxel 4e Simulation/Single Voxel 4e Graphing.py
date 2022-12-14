import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import seaborn as sns
import pandas as pd


SENSITIVE = 1
RESISTANT = 0
NOPROGRESSION = -1


def PopulationLinePlot(population, label=None):
   plt.plot(range(700), population[0:700], label=label)

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

Deaths = [0.0, 0.00625, 0.0135]
Costs = [0.15, 0.075, 0.05, 0.01]
DEATH_RATE = 0.0135
COST_OF_RESISTANCE = 0.01

SIDE = 5
DENSITY = 0.1
INITSENSITIVE = 74992
INITRESISTANT = 7
SingleVoxelAdaptiveData = np.loadtxt(
        fr"SingleVoxelFig4AdaptiveTherapy_{SIDE}side_somespace_{DEATH_RATE}death_{COST_OF_RESISTANCE}cost_{DENSITY}density_{INITSENSITIVE}initsensitive_{INITRESISTANT}initresistant.csv",
        delimiter=",")
SingleVoxelContinuousData = np.loadtxt(
        fr"SingleVoxelFig4ContinuousTherapy_{SIDE}side_somespace_{DEATH_RATE}death_{COST_OF_RESISTANCE}cost_{DENSITY}density_{INITSENSITIVE}initsensitive_{INITRESISTANT}initresistant.csv",
        delimiter=",")
def ContTTPvsAdapTTPLinePlot(adapdata, contdata):
    INIT_TOTAL_POP = adapdata[RESISTANT, 0] + adapdata[SENSITIVE, 0]
    if INIT_TOTAL_POP != contdata[RESISTANT, 0] + contdata[SENSITIVE, 0]: print("Initial populations are different")
    PopulationLinePlot(adapdata[RESISTANT], "Resistant Cells")
    PopulationLinePlot(adapdata[SENSITIVE], "Sensitive Cells")
    PopulationLinePlot(adapdata[SENSITIVE] + adapdata[RESISTANT], "Total Cells")
    plt.title(f"50% tumor dens, 10% init res, {DENSITY} Density, {DEATH_RATE} death, {COST_OF_RESISTANCE} cost, {SIDE} side")
    TTPAdap = int(TTP(adapdata, 1.2*INIT_TOTAL_POP, 0))
    plt.axvline(TTPAdap, ymin=0, color='red', label='adaptive TTP', linestyle='dotted')
    TTPCont = int(TTP(contdata, 1.2*INIT_TOTAL_POP, 0))
    plt.axvline(TTPCont, ymin=0, color='blue', label='continuous TTP', linestyle='dotted')
    plt.legend()
    plt.show()


ContTTPvsAdapTTPLinePlot(SingleVoxelAdaptiveData, SingleVoxelContinuousData)
