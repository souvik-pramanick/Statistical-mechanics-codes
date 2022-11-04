#central limit exercise 541

import numpy as np
import matplotlib.pyplot as plt

sample_mean=lambda n:np.mean(np.random.uniform(0,2,size=n))

x1=[sample_mean(1) for i in range(10000)]
x2=[sample_mean(2) for i in range(10000)]
x3=[sample_mean(5) for i in range(10000)]
x4=[sample_mean(50) for i in range(10000)]

plt.subplot(2,2,1)
plt.hist(x1,bins=30,ec='k',color='red')

plt.subplot(2,2,2)
plt.hist(x2,bins=30,ec='k',color='blue')

plt.subplot(2,2,3)
plt.hist(x3,bins=30,ec='k',color='yellow')

plt.subplot(2,2,4)
plt.hist(x4,bins=30,ec='k',color='green')

plt.show()
