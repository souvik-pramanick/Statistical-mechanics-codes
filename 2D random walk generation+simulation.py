#Generate a 2D random walk
from random import choice
import numpy as np
import matplotlib.pyplot as plt

x,y=0,0 #starting position
X,Y=[x],[y]


for i in range(5000):
	dx, dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
	x,y=x+dx,y+dy
	X.append(x)
	Y.append(y)
	plt.cla()
	plt.plot(X,Y,'o')
	plt.plot(X,Y)
	plt.pause(0.001)
	

	

	