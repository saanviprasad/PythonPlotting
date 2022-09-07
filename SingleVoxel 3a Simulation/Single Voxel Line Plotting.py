import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import seaborn as sns
import pandas as pd


SENSITIVE = 1
RESISTANT = 0


#def PopulationLinePlot(population, label=None):
 #   plt.plot(range(len(population)), population, label=label)


data = []
Init_Res_Populations = [250, 500, 750, 2500, 5000, 7500, 25000, 50000, 75000]
Init_Sens_Populations = [249750, 499500, 749250, 247500, 495000, 742500, 225000, 450000, 675000]
RESPOP = 75000
SENSPOP = 675000
SingleVoxelData = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\SingleVoxel 3a Simulation\SingleVoxelAdaptiveTherapy_0.5density_nocost_{SENSPOP}initsensitive_{RESPOP}initresistant1.csv", delimiter=",")
data.append(SingleVoxelData)
for i,f in enumerate(data):
    PopulationLinePlot(f[RESISTANT], "Resistant Cells")
for i,f in enumerate(data):
    PopulationLinePlot(f[SENSITIVE], "Sensitive Cells")
for i,f in enumerate(data):
    PopulationLinePlot(f[SENSITIVE]+f[RESISTANT], "Total Cells")
plt.title(f"{RESPOP} Init Res, {SENSPOP} Init Sens, 0.5 Density")
plt.legend()
plt.show()
