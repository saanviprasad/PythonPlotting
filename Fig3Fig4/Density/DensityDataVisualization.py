import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams.update({'axes.titlesize':'medium'})
plt.rcParams.update({'figure.titlesize':'medium'})
plt.rc("axes.spines",top=False,right=False)
matplotlib.rcParams['font.family']='Calibri'
matplotlib.rcParams['font.size']=11
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams['figure.dpi'] = 300
def SubsetScatter(data,color):
    sns.kdeplot(data,x='ProgAdap',y='ProgCont')
    plt.axline((0,0),(1,1),zorder=0)


Data = pd.read_csv("DensityResults.csv")

grid = sns.FacetGrid(Data, row="density")

grid.map_dataframe(SubsetScatter)
plt.show()