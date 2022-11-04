#Plot Histogram for normal(Gaussian) random numbers

#A very funny game made by me based on chance and choice

import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(1,4,100000)
n=np.linspace(-20,20,100000)
f=8800*np.exp(-(n-1)**2/(2*4**2))
plt.plot(n,f)
plt.hist(x,bins=40,rwidth=0.8,histtype='bar')
plt.show()