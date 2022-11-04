#How the distribution depends on system size

import numpy as np
import matplotlib.pyplot as plt



#function to create a list of heads
f=lambda n:[sum(np.random.randint(0,2,size=n)) for i in range(trials)]

n,trials=10,10000

markers=['o','^','p']

for i in range(3):
	x,y=np.unique(f(n),return_counts=True)
	x=x/n
	y=y/np.max(y)
	n=10*n
	plt.plot(x,y,marker=markers[i])
plt.legend(['n=10','n=100','n=1000'])
plt.show()