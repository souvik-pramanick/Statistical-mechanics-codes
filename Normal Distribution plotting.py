import numpy as np
x=np.random.randn(100000)
y=np.random.normal(0,1,100000)
z=np.random.normal(1,1,100000)
import matplotlib.pyplot as plt
plt.subplot(2,2,(1,2))
plt.hist(x,bins=20,ec='red')

plt.subplot(2,2,3)
plt.hist(y,bins=20,ec='blue')

plt.subplot(2,2,4)
plt.hist(z,bins=20,ec='yellow')
plt.show()
