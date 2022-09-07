import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import seaborn as sns
import pandas as pd
SENSITIVE = 1
RESISTANT = 0
NOPROGRESSION = -1



def ContvsAdaptiveHeatMap(density, sensprolif, resprolif, sensresource, resresource):
    prolifexp = np.array([1.0, 1.5, 2.0, 2.5])
    moverate = np.array(["1.0E-4","1.0E-5", "1.0E-6", "1.0E-7"])
    heatmapData1 = np.zeros([len(moverate), len(prolifexp)])
    heatmapData2 = np.zeros([len(moverate), len(prolifexp)])
    for i, move in enumerate(moverate):
        for j, prolif in enumerate(prolifexp):
            TTPValueAdap = np.loadtxt(
                fr"C:\Users\Administrator\PycharmProjects\pythonProject2\AdaptiveTherapyParamSweep\AdaptiveTherapy_{density}density_{prolif}prolifexp_{move}moverate_{sensprolif}sensprolif_{resprolif}resprolif_{sensresource}sensresource_{resresource}resresource.csv",
                delimiter=",")
            heatmapData1[i, j] = TTP(TTPValueAdap, 144000000, 120000000)
    for i, move in enumerate(moverate):
        for j, prolif in enumerate(prolifexp):
            TTPValueCont = np.loadtxt(
                fr"C:\Users\Administrator\PycharmProjects\pythonProject2\ContinuousTherapyParamSweep\ContinuousTherapy_{density}density_{prolif}prolifexp_{move}moverate_{sensprolif}sensprolif_{resprolif}resprolif_{sensresource}sensresource_{resresource}resresource.csv",
                delimiter=",")
            heatmapData2[i, j] = TTP(TTPValueCont, 144000000, 120000000)
    heatmapData3 = heatmapData1 - heatmapData2
    plt.subplot(1, 3, 1)
    HeatMap(heatmapData1, prolifexp, moverate, "Proliferation Exponent", "Movement Rate Base",
            "Adaptive Therapy", "TTP")
    plt.subplot(1, 3, 2)
    HeatMap(heatmapData2, prolifexp, moverate, "Proliferation Exponent", None,
            "Continuous Therapy", "TTP")
    plt.subplot(1, 3, 3)
    HeatMap(heatmapData3, prolifexp, moverate, "Proliferation Exponent", None,
            "Adaptive-Continuous Therapy", "TTP")
    plt.suptitle(f"{density} Density, {sensprolif} Sensprolif, {resprolif} Resprolif, {sensresource} Sensresource, {resresource} Resresource")
    plt.ticklabel_format()
    plt.show()

ContvsAdaptiveHeatMap(0.1, 0.15, 0.15, 0.3, 0.3)

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

