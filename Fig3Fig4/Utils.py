import matplotlib.pyplot as plt
import pandas as pd

def PopulationLinePlot(population, label=None):
   plt.plot(range(700), population[0:700], label=label)

def IterDf(df):
   rows=df.to_dict('records')
   for row in rows: yield row