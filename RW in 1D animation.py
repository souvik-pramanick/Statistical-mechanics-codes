#RW in 1D animation

import numpy as np
import matplotlib.pyplot as plt

x=0
X=[x]

for t in range(10000):
	dx=np.random.choice([-1,1])
	x=x+dx
	X.append(x)
	
	plt.cla()
	plt.plot(X)
	plt.axhline(1)
	plt.pause(0.001)