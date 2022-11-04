import numpy as np
import matplotlib.pyplot as plt

x=np.mean(np.random.random(size=(100000,100)),axis=1)

plt.hist(x,bins=20,ec='yellow',color='red',rwidth=0.8)
plt.show()