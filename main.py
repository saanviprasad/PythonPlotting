# import numpy as np
# import matplotlib.pyplot as plt
# from tabulate import tabulate
# import seaborn as sns
# import pandas as pd
# SENSITIVE = 1
# RESISTANT = 0
# NOPROGRESSION = -1
# ON_OFF_PATH=fr"C:\Users\Administrator\PycharmProjects\pythonProject2\DensityAndConcentrationSweep1On3Off"
# CONSTANT_PATH=fr"C:\Users\Administrator\PycharmProjects\pythonProject2\DensityAndConcentrationSweep"
#
# def PopulationLinePlot(population,label=None): plt.plot(range(len(population)),population,label=label)
#
#
# def StackPlotPopulations(populations,labels=("resistant", "sensitive")):
#     plt.gca().stackplot(range(len(populations[0])), populations, labels = labels)
#
# def TTP(populations, progressionpop, startpopulation):
#     TOTAL = populations[RESISTANT] + populations[SENSITIVE]
#     for day, pop in enumerate(TOTAL):
#         if pop > progressionpop:
#             for start, pop in enumerate(TOTAL):
#                 if pop > startpopulation:
#                     DRUGSTART = start
#                     TIME = day - DRUGSTART
#                     return TIME
#     return NOPROGRESSION
#
# def GetData(path,density,conc,trial):
#     densityStr="{:.2f}".format(density)
#     concStr="{:.2f}".format(conc)
#     return np.loadtxt(fr"{path}\DrugConcentrationResponse{densityStr}_{concStr}_{trial}.csv",delimiter=",")
#
# def HeatMap(data, xticks, yticks, xlabel, ylabel, title, colorbarlabel):
#     ax = plt.gca()
#     im = ax.imshow(data)
#     ax.set_xticks(np.arange(len(xticks)), labels=xticks)
#     ax.set_yticks(np.arange(len(yticks)), labels=yticks)
#     ax.set_xlabel(xlabel)
#     ax.set_ylabel(ylabel)
#     plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
#
#     for i,_ in enumerate(yticks):
#         for j,_ in enumerate(xticks):
#             ax.text(j, i, f"{int(data[i, j])}", ha="center", va="center", color="w", size=5)
#     ax.set_title(title)
#
#
# def ContvsAdaptiveHeatMap(density, sensprolif, resprolif, sensresource, resresource):
#     prolifexp = np.array([1.0, 1.5, 2.0, 2.5])
#     moverate = np.array(["1.0E-4","1.0E-5", "1.0E-6", "1.0E-7"])
#     heatmapData1 = np.zeros([len(moverate), len(prolifexp)])
#     heatmapData2 = np.zeros([len(moverate), len(prolifexp)])
#     for i, move in enumerate(moverate):
#         for j, prolif in enumerate(prolifexp):
#             TTPValueAdap = np.loadtxt(
#                 fr"C:\Users\Administrator\PycharmProjects\pythonProject2\AdaptiveTherapyParamSweep\AdaptiveTherapy_{density}density_{prolif}prolifexp_{move}moverate_{sensprolif}sensprolif_{resprolif}resprolif_{sensresource}sensresource_{resresource}resresource.csv",
#                 delimiter=",")
#             heatmapData1[i, j] = TTP(TTPValueAdap, 144000000, 120000000)
#     for i, move in enumerate(moverate):
#         for j, prolif in enumerate(prolifexp):
#             TTPValueCont = np.loadtxt(
#                 fr"C:\Users\Administrator\PycharmProjects\pythonProject2\ContinuousTherapyParamSweep\ContinuousTherapy_{density}density_{prolif}prolifexp_{move}moverate_{sensprolif}sensprolif_{resprolif}resprolif_{sensresource}sensresource_{resresource}resresource.csv",
#                 delimiter=",")
#             heatmapData2[i, j] = TTP(TTPValueCont, 144000000, 120000000)
#     heatmapData3 = heatmapData1 - heatmapData2
#     plt.subplot(1, 3, 1)
#     HeatMap(heatmapData1, prolifexp, moverate, "Proliferation Exponent", "Movement Rate Base",
#             "Adaptive Therapy", "TTP")
#     plt.subplot(1, 3, 2)
#     HeatMap(heatmapData2, prolifexp, moverate, "Proliferation Exponent", None,
#             "Continuous Therapy", "TTP")
#     plt.subplot(1, 3, 3)
#     HeatMap(heatmapData3, prolifexp, moverate, "Proliferation Exponent", None,
#             "Adaptive-Continuous Therapy", "TTP")
#     plt.suptitle(f"{density} Density, {sensprolif} Sensprolif, {resprolif} Resprolif, {sensresource} Sensresource, {resresource} Resresource")
#     plt.ticklabel_format()
#     plt.show()
#
# ContvsAdaptiveHeatMap(0.1, 0.15, 0.15, 0.3, 0.3)
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






# AdapContData = []
# Therapies = ["Adaptive", "Continuous"]
# for i in range (0,2):
#     Data = np.loadtxt(fr"C:\Users\Administrator\PycharmProjects\pythonProject2\{Therapies[i]}TherapyParamSweep\{Therapies[i]}Therapy_0.1density_1.0prolifexp_1.0E-4moverate_0.15sensprolif_0.1resprolif_0.3sensresource_0.3resresource.csv", delimiter=",")
#     AdapContData.append(Data)
# print(TTP(Data, 144000000))




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
#
# for i,f in enumerate(files):
#     PopulationLinePlot(f[SENSITIVE], f"{startpopulations[i]}")
# plt.title("Sensitive Cell Population")
# plt.legend()
# plt.show()
# for i,f in enumerate(files):
# #plt.plot(range(len(f[SENSITIVE])), f[SENSITIVE]+f[RESISTANT], label=f"Start Population {startpopulations[i]} million")
#     PopulationLinePlot(f[SENSITIVE]+f[RESISTANT], f"{startpopulations[i]}")
# plt.legend()
# plt.title("Total Cell Population")
# plt.show()




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
#
# resistive = []
# resistive2 = []
# resistive3 = []
# resistive4 = []
# resistive5 = []
#with open('C:\Users\Administrator\PycharmProjects\pythonProject2\DensityAndConcentrationSweep\DrugConcentrationResponse0.10_0.25_0.csv', 'r') as f:

#f = np.loadtxt("C:\Users\Administrator\PycharmProjects\pythonProject2\DensityAndConcentrationSweep\DrugConcentrationResponse0.10_0.25_0.csv",delimiter="\n")
#for line in f:
#    resistiveline = line.rstrip().split('\t')
#    resistive.append(resistiveline)
#print(resistive)




#ignore these for l
#oops just use the thing above this
# for i in range(0,9):
#     GetData2 = GetData(CONSTANT_PATH, densities[i],0.25,0)
#     resistive2.append(GetData2[1,1000])
# for i in range(0,9):
#     GetData3 = GetData(CONSTANT_PATH, densities[i],0.50,0)
#     resistive3.append(GetData3[1,1000])
# for i in range(0,9):
#     GetData4 = GetData(CONSTANT_PATH, densities[i],0.75,0)
#     resistive4.append(GetData4[1,1000])
# for i in range(0,9):
#     GetData5 = GetData(CONSTANT_PATH, densities[i],1.00,0)
#     resistive5.append(GetData5[1,1000])


#plt.imshow(adamsmomishot, cmap='hot', interpolation='nearest')
#plt.show()
#adamsmomishot = np.hstack([resistive, resistive2, resistive3, resistive4, resistive5]).reshape(9, 5).tolist()
#adamsmomishot = [resistive, resistive2, resistive3, resistive4, resistive5]
#adamsmomishot =
#adamsmomishot = np.concatenate(resistive2)
#adamsmomishot = np.reshape(9,1)
#print(adamsmomishot)
#resistive = np.array(resistive)

# ax=plt.gca()
# im = ax.imshow(heatmapData1)
# ax.set_xticks(np.arange(len(prolifexp)), labels=prolifexp)
# ax.set_yticks(np.arange(len(moverate)), labels=moverate)
# #
# plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
#
# for i,move in enumerate(moverate):
#     for j,prolif in enumerate(prolifexp):
# #       text = ax.text(j, i, f"{heatmapData1[i,j]:.2e}", ha="center", va="center", color="w")
#        text = ax.text(j, i, f"{int(heatmapData1[i,j])}", ha="center", va="center", color="w")
# ax.set_title("TTP of Adaptive Therapy Based on Prolif Exponent and Moverate at all Defaults")

# bar = plt.colorbar(im)
# bar.set_label("TTP")
# plt.subplot(1,2,2)
# ax=plt.gca()
# im = ax.imshow(heatmapData2)
# ax.set_xticks(np.arange(len(prolifexp)), labels=prolifexp)
# ax.set_yticks(np.arange(len(moverate)), labels=moverate)
# #
# plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
#
# for i,move in enumerate(moverate):
#     for j,prolif in enumerate(prolifexp):
#        ax.text(j, i, f"{int(heatmapData2[i,j])}", ha="center", va="center", color="w")
#
# ax.set_title("TTP of Continuous Therapy Based on Prolif Exponent and Moverate at all Defaults")
#
# bar = plt.colorbar(im)
# bar.set_label("TTP")
#
# plt.show()



#x=GetData(CONSTANT_PATH,0.1,1.00,1)
#densities = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
#concentration = np.array([0.00, 0.25, 0.50, 0.75, 1.00])

#StackPlotPopulations(x,["res","sen"])
#plt.legend()
#plt.show()

