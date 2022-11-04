#many random walks
import matplotlib.pyplot as plt
import numpy as np

def walk(n):
	x=np.random.choice([-1,1],size=n)
	return np.cumsum(x)
	
n=10000

end2end=[walk(n)[-1] for _ in range(100000)]
plt.hist(end2end,bins=50,color='white')
plt.show()


