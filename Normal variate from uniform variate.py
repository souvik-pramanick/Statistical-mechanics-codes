#transformation from uniform to normal variate

import numpy as np
import matplotlib.pyplot as plt

n=10000

x1=np.random.random(n)
x2=np.random.random(n)

theta=2*np.pi*x2

r=np.sqrt(-2*np.log(x1))

z1,z2=r*np.cos(theta),r*np.sin(theta)

plt.suptitle('Normal variate from uniform')
plt.subplot(2,2,1)
plt.hist(z1,bins=30,ec='k',edgecolor='w',color='red',rwidth=0.8,label='z1')
plt.legend(loc='best')

plt.subplot(2,2,3)
plt.hist(z2,bins=30,ec='k',edgecolor='w',color='red',rwidth=0.8,label='z2')
plt.legend(loc='best')

plt.subplot(2,2,(2,4))
plt.scatter(z1,z2,c='k',label='scatter plot')
plt.legend(loc='best')
plt.xlabel('z1')
plt.ylabel('z2')

plt.show()


