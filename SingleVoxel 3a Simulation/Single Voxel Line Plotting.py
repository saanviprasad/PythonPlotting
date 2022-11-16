import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import seaborn as sns
import pandas as pd


SENSITIVE = 1
RESISTANT = 0
NOPROGRESSION = -1


def PopulationLinePlot(population, label=None):
   plt.plot(range(700),population[0:700], label=label)

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


Init_Res_Populations = [13, 25, 38, 12500, 25000, 37500, 62500, 125000, 187500]
Init_Sens_Populations = [124988, 249975, 374963, 112500, 225000, 337500, 62500, 125000, 187500]
init_res_pops_low = [3, 5, 8, 2500, 5000, 7500, 12500, 25000, 37500 ]
init_sens_pops_low = [24998, 49995, 74993, 22500, 45000, 67500, 12500, 25000, 37500]
DENSITY = 0.5
DEATH = 0.00625
COST = 0.15
INIT_RES = 37500
INIT_SENS = 337500
SIDE = 5
SingleVoxelAdaptiveData = np.loadtxt(
fr"SingleVoxelAdaptiveTherapy_{DENSITY}density_nocost_{INIT_SENS}initsensitive_{INIT_RES}initresistant1.csv",
    delimiter=",")
SingleVoxelContinuousData = np.loadtxt(fr"SingleVoxelContinuousTherapy_{DENSITY}density_nocost_{INIT_SENS}initsensitive_{INIT_RES}initresistant1.csv",
    delimiter=",")
#SingleVoxelAdaptiveData = np.loadtxt(
   #     fr"SingleVoxelFig3AdaptiveTherapy_{SIDE}side_full_{DEATH}death_{COST}cost_{DENSITY}density_{INIT_SENS}initsensitive_{INIT_RES}initresistant.csv",
    #    delimiter=",")
# SingleVoxelContinuousData = np.loadtxt(
#         fr"SingleVoxelFig3ContinuousTherapy_{SIDE}side_full_{DEATH}death_{COST}cost_{DENSITY}density_{INIT_SENS}initsensitive_{INIT_RES}initresistant.csv",
#         delimiter=",")
def ContTTPvsAdapTTPLinePlot(adapdata, contdata):
    INIT_TOTAL_POP = adapdata[RESISTANT, 0] + adapdata[SENSITIVE, 0]
    if INIT_TOTAL_POP != contdata[RESISTANT, 0] + contdata[SENSITIVE, 0]: print("Initial populations are different")
    PopulationLinePlot(adapdata[RESISTANT], "Adap Resistant Cells")
    PopulationLinePlot(adapdata[SENSITIVE], "Adap Sensitive Cells")
    PopulationLinePlot(adapdata[SENSITIVE] + adapdata[RESISTANT], "Adap Total Cells")
#    PopulationLinePlot(contdata[RESISTANT]+contdata[SENSITIVE], "Cont Total Cells")
    plt.title(f"{adapdata[RESISTANT, 0]} Init Res, {adapdata[SENSITIVE, 0]} Init Sens, {DENSITY} Density, No Cost")
    TTPAdap = int(TTP(adapdata, 1.2*INIT_TOTAL_POP, 0))
    plt.axvline(TTPAdap, ymin=0, color='red', label='adaptive TTP', linestyle='dotted')
    TTPCont = int(TTP(contdata, 1.2*INIT_TOTAL_POP, 0))
    plt.axvline(TTPCont, ymin=0, color='blue', label='continuous TTP', linestyle='dotted')
    plt.legend()
    plt.show()


ContTTPvsAdapTTPLinePlot(SingleVoxelAdaptiveData, SingleVoxelContinuousData)

# data = []
#
# RESPOP = 125
# SENSPOP = 124875
# SingleVoxelAdaptiveData = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\SingleVoxel 3a Simulation\SingleVoxelAdaptiveTherapy_0.5density_nocost_{SENSPOP}initsensitive_{RESPOP}initresistant1.csv", delimiter=",")
# data.append(SingleVoxelAdaptiveData)
# for i,f in enumerate(data):
#     PopulationLinePlot(f[RESISTANT], "Resistant Cells")
# for i,f in enumerate(data):
#     PopulationLinePlot(f[SENSITIVE], "Sensitive Cells")
# for i,f in enumerate(data):
#     PopulationLinePlot(f[SENSITIVE]+f[RESISTANT], "Total Cells")
# plt.title(f"{RESPOP} Init Res, {SENSPOP} Init Sens, 0.5 Density")
# TTPAdap = int(TTP(SingleVoxelAdaptiveData, (1.2*(RESPOP+SENSPOP)), (RESPOP+SENSPOP)))
# SingleVoxelContinuousData = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\SingleVoxel 3a Simulation\SingleVoxelContinuousTherapy_0.5density_nocost_{SENSPOP}initsensitive_{RESPOP}initresistant1.csv", delimiter=",")
# plt.axvline(TTPAdap, ymin=0, color='red', label= 'adaptive TTP', linestyle='dotted')
# TTPCont = int(TTP(SingleVoxelContinuousData, (1.2*(RESPOP+SENSPOP)), (RESPOP+SENSPOP)))
# plt.axvline(TTPCont, ymin=0, color='blue', label= 'continuous TTP', linestyle='dotted')
# plt.legend()
# plt.show()
