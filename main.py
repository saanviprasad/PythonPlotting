import numpy as np
import matplotlib.pyplot as plt

x=np.loadtxt(r"C:\Users\Administrator\Documents\GitHub\AgentFramework\TargetedTherapyData.csv", delimiter=",")
print("done")
totalCells=x[0]+x[1]
plt.plot(range(100),x[0], label="resistant cells")
plt.plot(range(100),x[1], label="sensitive cells")
plt.plot(range(100),totalCells, label="total cells")

plt.legend()
plt.show()
