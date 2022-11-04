#MC integration distribution of results

import numpy as np

def MCI(f,a,b):
	N=10000
	x=np.random.uniform(a,b,N)
	return (b-a)*np.mean(f(x))
	

f=lambda x:np.sin(x)
a,b=0,np.pi
val=MCI(f,a,b)
#print(val)

#distribution
import matplotlib.pyplot as plt
X=[MCI(f,a,b) for i in range(10000)]
with plt.xkcd():
	plt.hist(X,bins=40,color='k',ec='yellow')
	plt.show()
	


	

	