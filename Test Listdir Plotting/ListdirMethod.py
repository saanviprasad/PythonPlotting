import os
import numpy as np
from Utils import *
#C:\Users\Administrator\PycharmProjects\pythonProject2\Single Voxel 4e Simulation
filenames = []
EXPERIMENT_FOLDER = "ExampleExperiment"
for filename in os.listdir(EXPERIMENT_FOLDER):
    if filename[-4:] == ".csv":
        filenames.append(filename)
        print(filename.split("_"))
for i in range (len(filenames)):
    filenames[i] = fr"{EXPERIMENT_FOLDER}\{filenames[i]}"
plt.figure(figsize=(16,9), dpi=30)
for i in range (len(filenames)//2):
    AdaptiveData = np.loadtxt(filenames[i], delimiter=",")
    ContinuousData = np.loadtxt(filenames[i+len(filenames)//2], delimiter=",")
    plt.subplot(4, 3, i+1)
    PopulationLinePlot(AdaptiveData[0],"Adap Resistant Cells")
    PopulationLinePlot(AdaptiveData[1], "Adap Sensitive Cells")
    PopulationLinePlot(ContinuousData[0], "Cont Resistant Cells")
    PopulationLinePlot(ContinuousData[1], "Cont Sensitive Cells")
    Namecomponents = filenames[i].split("_")
    Namecomponents[-1] = Namecomponents[-1][0:-4]
    plt.title(" ".join(Namecomponents[2:8]))


#plt.savefig("test.png")
plt.tight_layout()
plt.show()