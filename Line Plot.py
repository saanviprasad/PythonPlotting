import numpy as np
import matplotlib.pyplot as plt
SENSITIVE = 1
RESISTANT = 0
NOPROGRESSION = -1

def PopulationLinePlot(population,label=None): plt.plot(range(len(population)),population,label=label)

#these two functions are for data extraction purposes
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
#Example
# AdapContData = []
# Therapies = ["Adaptive", "Continuous"]
# for i in range (0,2):
#     Data = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\{Therapies[i]}TherapyParamSweep\{Therapies[i]}Therapy_0.1density_1.0prolifexp_1.0E-4moverate_0.15sensprolif_0.1resprolif_0.3sensresource_0.3resresource.csv", delimiter=",")
#     AdapContData.append(Data)
# print(TTP(Data, 144000000))
def GetData(path,density,conc,trial):
    densityStr="{:.2f}".format(density)
    concStr="{:.2f}".format(conc)
    return np.loadtxt(fr"{path}\DrugConcentrationResponse{densityStr}_{concStr}_{trial}.csv",delimiter=",")



#Example of Line Plot
# files = []
# startpopulations = [30000000, 60000000, 90000000, 120000000]
# #for i in range(0,4):
# ContinuousTherapyData = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\ContinuousTherapyTrials\ContinuousTrials30000000Start_1.0Drug_0.1Density.csv",delimiter=",")
# files.append(AdaptiveTherapyData)
# files.append(ContinuousTherapyData)
# #for i in range(0,4):
# #Therapies = ["Continuous Therapy", "Adaptive Therapy"]
# for i, f in enumerate(files):
#     PopulationLinePlot(f[RESISTANT],f"{startpopulations[i]}")
# #plt.plot(range(len(f[RESISTANT])), f[RESISTANT], label=f'Start Population {startpopulations[i]} million')
# plt.title("Resistant Cell Population")
# plt.legend()
# plt.show()

#Example two
#for i in range (10):
#for i,f in enumerate(files):
 #   PopulationLinePlot(f[RESISTANT],f"lung density {(i+1)/10.0}")
#    plt.plot(range(len(f[RESISTANT])), f[RESISTANT], label=f"lung density {(i+1)/10.0}")
#plt.legend()
#plt.title("Resistant Cell Population")
# plt.show()
# for i,f in enumerate(files):
#     plt.plot(range(len(f[SENSITIVE])), f[SENSITIVE], label=f"lung density {(i+1)/10.0}")
# plt.legend()
# plt.title("Sensitive Cell Population")
# plt.show()
# for i,f in enumerate(files):
#    plt.plot(range(len(f[SENSITIVE])), f[SENSITIVE]+f[RESISTANT], label=f"lung density {(i+1)/10.0}")
# plt.legend()
# plt.title("Total Cell Population")
# plt.show()
