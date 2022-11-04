#stacked Gaussian distributions


import numpy as np
import matplotlib.pyplot as plt

x=np.random.randn(10000,16)
colors=[ "black", "red", "green", "blue", "cyan", "yellow", "magenta","k","black", "red", "green", "blue", "cyan", "yellow", "magenta","k"]
plt.hist(x,bins=40,color=colors,rwidth=0.8,histtype='bar',stacked=True,edgecolor='black')


plt.show()