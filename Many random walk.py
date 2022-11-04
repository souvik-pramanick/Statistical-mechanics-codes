#many random walks
import matplotlib.pyplot as plt
import numpy as np

def walk(n):
	x=np.random.choice([-1,1],size=n)
	return np.cumsum(x)
	
n=10000

for i in range(100):
	plt.plot(walk(n),lw=0.5)
plt.xlim(0,10000)

plt.show()


