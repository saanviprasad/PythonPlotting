import matplotlib.pyplot as plt

def PopulationLinePlot(population, label=None):
   plt.plot(range(700), population[0:700], label=label)