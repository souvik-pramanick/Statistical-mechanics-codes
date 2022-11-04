#many random walks
import matplotlib.pyplot as plt
import numpy as np

def walk(n):
	x=np.random.choice([-1,1],size=n)
	return np.cumsum(x)
	
n=10000

plt.subplot(1,2,1)
for i in range(100):
	plt.plot(walk(n), lw=0.5)
	plt.xlim(0,10000)

end2end=[walk(n)[-1] for _ in range(100000)]
plt.subplot(1,2,2)
plt.hist(end2end,bins=50,color='white',ec='k')
plt.show()




