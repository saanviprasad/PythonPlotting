import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from Utils import IterDf
from numba import njit
import seaborn as sns

plt.rcParams.update({'axes.titlesize':'medium'})
plt.rcParams.update({'figure.titlesize':'medium'})
plt.rc("axes.spines",top=False,right=False)
matplotlib.rcParams['font.family']='Calibri'
matplotlib.rcParams['font.size']=11
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams['figure.dpi'] = 300

CONT_RES=0
CONT_TOT=1
ADAP_RES=2
ADAP_TOT=3

def FolderToDataFrame(path,*types):
    files=[f for f in os.listdir(path) if f[-4:]=='.csv']
    return FileNamesToDataFrame(path,files,*types)


def FileNamesToDataFrame(path,files,*types):
    fileData=[]
    for file in files:
        fileSplit=file.split("~")
        fileData.append([types[i](fileSplit[i*2+1]) for i in range(len(fileSplit)//2)]+[rf"{path}/{file}"])
    return pd.DataFrame(fileData,columns=[fileSplit[i*2] for i in range(len(fileSplit)//2)]+['path'])

def PlotPops(path):
    data=np.loadtxt(path,delimiter=",")
    progCont=GetProgressionDate(data,CONT_TOT)
    progAdap=GetProgressionDate(data,ADAP_TOT)
#    progCont=len(data[0])
#    progAdap=len(data[0])
#    progressionCont=data[CONT_TOT,0]*1.2
#    progressionAdap=data[ADAP_TOT,0]*1.2
#    for i in range(len(data[0])):
#        if progCont==len(data[0]) and data[CONT_TOT,i]>progressionCont: progCont=i
#        if progAdap==len(data[0]) and data[ADAP_TOT,i]>progressionAdap: progAdap=i
    plt.axvline(x=progAdap,color='r')#,label='adap progression')
    plt.axvline(x=progCont,linestyle='--',color='b')#,label='cont progression')
    maxProg=max(progCont,progAdap)
    ticks=np.arange(0,maxProg)
    plt.plot(ticks,data[ADAP_TOT,:maxProg],color='r',label='adap total')
    plt.plot(ticks,data[CONT_TOT,:maxProg],color='b',linestyle='--',label='cont total')
    plt.plot(ticks,data[ADAP_RES,:maxProg],color='r',linestyle=':',label='adap res')
    plt.plot(ticks,data[CONT_RES,:maxProg],color='b',linestyle=':',label='cont res')
#    plt.legend()

def InitPopSubFigsFig3(data,side,margin):
    plt.figure(figsize=[8,9])
    data=data[(data.sideLen==side) & (data.margin==margin)].reset_index(drop=True)
    for i,row in data.iterrows():
        plt.subplot(3,3,i+1)
        PlotPops(row['path'])
        plt.title(f"Sen: {row['initSens']} Res: {row['initRes']}")

def InitPopSubFigsFig4(data,side,margin):
    plt.figure(figsize=[8,9])
    data=data[(data.sideLen==side) & (data.margin==margin)].sort_values(by=['resDivRate','deathRate']).reset_index(drop=True)
    for i,row in data.iterrows():
        plt.subplot(3,3,i+1)
        PlotPops(row['path'])
        plt.title(f"DeathRate: {row['deathRate']} ResDivRate: {row['resDivRate']}")

def InitPopSubFigsMigVsDiff(data,idx):
    plt.figure(figsize=[8,9])
    data=data[data.idx==idx].sort_values(by=['idx']).reset_index(drop=True)
    for i,row in data.iterrows():
        plt.subplot(3,3,i+1)
        PlotPops(row['path'])
        plt.title(f"migRate: {row['migRate']} DiffRate: {row['diffRate']}")

def PreProcFig4(folder):
    fileData=[]
    for file in os.listdir(folder):
        if file[-4:]=='.csv' and '~DeathRate~' in file:
            fileSplit=file.split("~")
            fileData.append([int(fileSplit[1]),int(fileSplit[3]),float(fileSplit[5]),float(fileSplit[7]),folder+file])
    return pd.DataFrame(fileData,columns=['sideLen','margin','deathRate','resDivRate','path'])

def PreProcFig3(folder):
    fileData=[]
    for file in os.listdir(folder):
        if file[-4:]=='.csv' and '~Sens~' in file:
            fileSplit=file.split("~")
            fileData.append([int(fileSplit[1]),int(fileSplit[3]),int(fileSplit[5]),int(fileSplit[7]),folder+file])
    return pd.DataFrame(fileData,columns=['sideLen','margin','initSens','initRes','path'])

def PreProcMigVsDiff(folder):
    files=[f for f in os.listdir(folder) if f[-4:]=='.csv']
    return FileNamesToDataFrame(folder,files,int,int,int,int,float,float)

def PlotMigDiff(data):
    for idx,group in data.groupby('idx'):
        group=group.sort_values(by=['migRate','diffRate']).reset_index(drop=True).to_dict('records')
        plt.figure(figsize=[6.5,7.5])
        for i,row in enumerate(group):
            plt.subplot(3,3,i+1)
            PlotPops(row['path'])
            plt.title(f"migRate: {row['migRate']}, DiffRate: {row['diffRate']}")
        title=f"normal{group[0]['normMarg']}_sen{group[0]['senMarg']}_res{group[0]['resMarg']}"
        plt.suptitle(title)
        plt.tight_layout()
        plt.savefig(title+".svg")
        plt.clf()


def PlotDomain(data,sideLen,margin,prefix,PlotFn):
    PlotFn(data,sideLen,margin)
    title=f"{prefix}_sideLen{sideLen}_margin{margin}"
    plt.suptitle(title)
    plt.tight_layout()
    plt.savefig(title+".svg")

def GroupbyPlot(df,groupCol,xCol,yCol):
    for i,group in df.groupby(groupCol):
        title=f"{groupCol}_{i}"
        GridPlot(group,xCol,yCol,title)

def GridPlot(group,xCol,yCol,title):
    plt.figure(figsize=[12.8,9.6])
    group=group.sort_values(by=[xCol,yCol]).reset_index(drop=True)
    for j,row in enumerate(IterDf(group)):
        xDim=len(pd.unique(group[xCol]))
        yDim=len(pd.unique(group[yCol]))
        plt.subplot(xDim,yDim,j+1)
        PlotPops(row['path'])
        plt.title(f"{xCol}:{row[xCol]} {yCol}:{row[yCol]}")
    plt.suptitle(title)
    plt.tight_layout()
    plt.savefig(title+".svg")
    plt.clf()

@njit
def GetProgressionDate(data,iPop):
    startPop=data[iPop,0]
    endPop=startPop*1.2
    for i in range(1,len(data[iPop])):
        if data[iPop,i]>endPop:
            return i
    return len(data[iPop])

def MeltTimesteps(df):
    idVars=[]
    valueVars=[]
    for col in df.columns:
        if "~" in col:valueVars.append(col)
        else: idVars.append(col)
    melted=pd.melt(df,id_vars=idVars,value_vars=valueVars,var_name="label",value_name="measure")
    melted[['day','type']]=melted['label'].str.split("~",expand=True)
    melted['day']=melted['day'].astype(int)
    return melted.reset_index(drop=True)

def SubsetScatter(data,color):
    sns.kdeplot(data,x='ProgAdap',y='ProgCont')
    plt.axline((0,0),(1,1),zorder=0)

#df=FolderToDataFrame("SmallInitialTumor",int,int,float)
#df['progAdap']=df.apply(lambda row:GetProgressionDate(np.loadtxt(row['path'],delimiter=","),ADAP_TOT),axis=1)
#df['progCont']=df.apply(lambda row:GetProgressionDate(np.loadtxt(row['path'],delimiter=","),CONT_TOT),axis=1)
#df.to_csv("SmallInitialTumor/SmallInitialTumorSummary.csv",index=False)
#data=pd.read_csv("SmallInitialTumor/TumorSizeMutRate.csv")
#g=sns.FacetGrid(data=data,row='StartSize',col='MutRate')
#g.map_dataframe(SubsetScatter)
#g.add_legend()
#plt.show()
#data2=MeltTimesteps(data)
#print("here")

#data=pd.read_csv("Sweep/Sweep.csv")
#data=data.groupby(["mutProb","moveDiscount","divDiscount","migExp","divExp"],as_index=False).mean()
#pd.to_pickle(data,"Sweep/SweepAvg.p")

"""Sweep Summary"""
#data=pd.read_pickle("Sweep/SweepAvg.p")
#sns.scatterplot(data=data,x='ProgAdap',y='ProgCont')
#plt.axline((0,0),(1,1),zorder=0)
#plt.show()

"""Plot of AT Better Subset"""
#data=pd.read_pickle("Sweep/SweepAvg.p")
#params=["mutProb","moveDiscount","divDiscount","migExp","divExp"]
#data['AdapContRatio']=data['ProgAdap']/data['ProgCont']
##print(len(data))
#data=data[data.AdapContRatio>1]
##print(len(data))
##sns.scatterplot(data=data,x='ProgAdap',y='AdapContRatio')
##plt.axline((0,0),(1,1),zorder=0)
##plt.show()
#
#for i,param in enumerate(params):
#    plt.subplot(2,3,i+1)
#    sns.scatterplot(data=data,x='AdapContRatio',y=param,hue='AdapContRatio',legend=False)
#plt.tight_layout()
#plt.show()

"""SweepII plot"""
data=pd.read_csv("SweepII/SweepII.csv")
g=sns.FacetGrid(data=data,row='mutProb',col='divTumor',sharey=False,sharex=False)
g.map_dataframe(SubsetScatter)
plt.show()


#data=data[(data.id==49)&(data.moveDiscount==0.01)&(data.drugSwitch==0.9)]
#g=sns.FacetGrid(data=data,row='moveDiscount',col='drugSwitch',sharey=False,sharex=False)
##g.map_dataframe(sns.lineplot,'day','population','type',units='id',estimator=None)
#g.map_dataframe(sns.lineplot,'day','population','type')
#g.add_legend()
#plt.show()
#data=MeltTimesteps(data)
#data=data[(data.label.str.contains('Div'))|(data.label.str.contains('Mig'))]
#sns.lineplot(data,x='day',y='measure',hue='type')
#pd.to_pickle(data,"SmallInitialTumor/meltedSteps.p")
#data=pd.read_pickle("SmallInitialTumor/meltedSteps.p")
#data=pd.read_csv("SmallInitialTumor/WhenDoesAtWorkIII.csv")
#data=pd.read_csv("DivMigExp/MigDivExpTest.csv")
#data=MeltTimesteps(data)
#data=data.groupby(['divExp','migExp','type','day'],as_index=False).mean()
#g=sns.FacetGrid(data=data,row='divExp',col='migExp',sharey=False,sharex=False)
#g.map_dataframe(SubsetScatter)
#print("here")
#g.map_dataframe(sns.lineplot,'day','measure','type',estimator=None)
#g.map_dataframe(sns.lineplot,'day','measure','type',units='id',estimator=None)
#data=pd.melt(data,id_vars=['idx','tumorSize','mutRate','path'],value_vars=['progAdap','progCont'],var_name='treatment',value_name='progression')
#g.add_legend()
#plt.tight_layout()
#plt.show()

#print("here")
#GridPlot(df,"mutRate","tumorSize","SmallInitialTumor")

#for i,group in df.groupby('tumorSize'):
#    group=group.sort_values(by=['res','sens']).reset_index(drop=True)
#    for j,row in enumerate(IterDf(group)):
#        plt.subplot(2,3,j+1)
#        PlotPops(row['path'])
#        plt.title(f"Init Sens:{row['sens']} Init Res:{row['res']}")
#    title=f"detectionSize_{i}"
#    plt.suptitle(title)
#    plt.tight_layout()
#    plt.savefig(title+".svg")
#    plt.clf()
#domains=[(1,0),(3,1),(3,0),(5,2),(5,1),(5,0)]
#data3=PreProcFig3("SlowerDeath/")
#for sideLen,margin in domains:
#    PlotDomain(data3,sideLen,margin,"Fig3",InitPopSubFigsFig3)
#data4=PreProcFig4("SlowerDeath/")
#for sideLen,margin in domains:
#    PlotDomain(data4,sideLen,margin,"Fig4",InitPopSubFigsFig4)
#data=PreProcMigVsDiff("MigVsDiff/")
#PlotMigDiff(data)
#print("here")
#for sideLen,margin in domains:
#    PlotDomain(data,sideLen,margin,"MigVsDiff",InitPopSubFigsMigVsDiff)

