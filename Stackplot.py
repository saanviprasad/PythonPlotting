import numpy as np
import matplotlib.pyplot as plt
SENSITIVE = 1
RESISTANT = 0
NOPROGRESSION = -1

def StackPlotPopulations(populations,labels=("resistant", "sensitive")):
    plt.gca().stackplot(range(len(populations[0])), populations, labels = labels)

# these two functions are for data extraction purposes
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

#Example
# AdaptiveData = []
# for i in range (0,6):
#     for j in range (1,5):
#         AdapData= np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\AdaptiveTherapyParamSweep\AdaptiveTherapy_{i/10}density_1.0prolifexp_1.0E-5moverate_0.15sensprolif_0.1resprolif_0.3sensresource_0.3resresource{j}.csv",
#                 delimiter=",")
#         AdapTTP = TTP(AdapData, 144000000, 120000000)
#         AdaptiveData.append(AdapTTP)
#     AdapData = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\AdaptiveTherapyParamSweep\AdaptiveTherapy_{i/10}density_1.0prolifexp_1.0E-5moverate_0.15sensprolif_0.1resprolif_0.3sensresource_0.3resresource.csv",
#                 delimiter=",")
#     AdapTTP = TTP(AdapData, 144000000, 120000000)
#     AdaptiveData.append(AdapTTP)
# ContinuousData = []
# for i in range (0,6):
#     for j in range (1,5):
#         ContData = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\ContinuousTherapyParamSweep\ContinuousTherapy_{i/10}density_1.0prolifexp_1.0E-5moverate_0.15sensprolif_0.1resprolif_0.3sensresource_0.3resresource{j}.csv",
#                 delimiter=",")
#         ContTTP = TTP(ContData, 144000000, 120000000)
#         ContinuousData.append(ContTTP)
#     ContData = np.loadtxt(
#         fr"C:\Users\Administrator\PycharmProjects\pythonProject2\ContinuousTherapyParamSweep\ContinuousTherapy_{i / 10}density_1.0prolifexp_1.0E-5moverate_0.15sensprolif_0.1resprolif_0.3sensresource_0.3resresource.csv",
#         delimiter=",")
#     ContTTP = TTP(ContData, 144000000, 120000000)
#     ContinuousData.append(ContTTP)
# AdaptiveVsContinuous = []
# for i in range(len(AdaptiveData)):
#     difference = AdaptiveData[i] - ContinuousData[i]
#     AdaptiveVsContinuous.append(difference)
# Densities = np.repeat([0.1,0.2,0.3,0.4,0.5,0.6],5)
# plt.scatter(Densities, AdaptiveVsContinuous, 5)
# z = np.polyfit(Densities, AdaptiveVsContinuous, 1)
# p = np.poly1d(z)
# plt.plot(Densities,p(Densities))
# plt.show()
