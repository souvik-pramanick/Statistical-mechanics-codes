import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(0,1,10000)
y=np.random.exponential(1,10000)
z=np.random.pareto(3.0,10000)

x1=x[::2]
x2=x[1::2]
y1=y[::2]
y2=y[1::2]
z1=z[::2]
z2=z[1::2]

plt.subplot(1,3,1)
plt.scatter(x1,x2,label='normal')
plt.legend(loc='best')

plt.subplot(1,3,2)
plt.scatter(y1,y2,label='exponential')
plt.legend(loc='best')

plt.subplot(1,3,3)
plt.scatter(z1,z2,label='pareto')
plt.legend(loc='best')

plt.show()






