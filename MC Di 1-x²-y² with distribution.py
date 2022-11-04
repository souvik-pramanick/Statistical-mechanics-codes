#MC double integral 1-x2-y2

import numpy as np

def MCI(f,a,b,c,d): 
	N=10000
	x=np.random.uniform(a,b,N)
	y=np.random.uniform(c,d,N)
	return np.mean(f(x,y))
	
f=lambda x,y:1-x**2-y**2

a,b,c,d=0,1,0,1
MCval=MCI(f,a,b,c,d)
#print(MCval)

#plot of results
import matplotlib.pyplot as plt
X=[MCI(f,a,b,c,d) for i in range(10000)]
with plt.xkcd():
	plt.hist(X,bins=40,color='red',ec='yellow')
	plt.show()

