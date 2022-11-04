#Radioactive Decay

def decay(N,time):
	population=[N]
	for t in range(1,time):
		r=np.random.random(N)
		survive=np.sum(r<q)
		population.append(survive)
		N=survive
	return np.array(population)
	
import numpy as np
import matplotlib.pyplot as plt

t_half=10
lam=np.log(2)/t_half
p=lam
q=1-p
N,time=1000,100

trials=range(10000)
mean_decay=np.mean([decay(N,time) for i in trials],axis=0)

plt.plot(range(time),mean_decay,lw=2)
plt.xlabel('Time',size=20)
plt.ylabel('Mean number',size=20)
plt.xlim(0,100)
plt.ylim(0,1000)
plt.show()
	
	