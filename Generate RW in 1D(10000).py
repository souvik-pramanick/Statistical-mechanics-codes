#Generate random walk in 1D of 10000 steps

import numpy as np

x=2*np.random.randint(0,2,size=10000)-1
cum=np.cumsum(x)

import matplotlib.pyplot as plt
plt.plot(cum)
plt.xlim(0,10000)

plt.show()