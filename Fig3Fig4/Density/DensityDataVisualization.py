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
plt.rcParams['figure.dpi'] = 100
#def SubsetScatter(data,color):

def SubsetScatter(data, color):
    sns.kdeplot(data = data,x='ProgAdap',y='ProgCont', hue = 'resgrowth')
    plt.axline((0,0),(1,1),zorder=0)


data = pd.read_csv("Phenotypes.csv")

fig = sns.FacetGrid(data= data ,row= 'angiopheno', col='glucpheno')
fig.map_dataframe(SubsetScatter)
plt.tight_layout()

plt.show()