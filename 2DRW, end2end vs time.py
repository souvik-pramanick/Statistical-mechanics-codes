#RW in 2D, end2end distance vs time

import numpy as np
import matplotlib.pyplot as plt
from random import choice

#defining single walk
def walk(steps):
	x,y=0,0
	X,Y=[],[]
	pos=[]
	for i in range(steps):
		dx,dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
		x,y=x+dx,y+dy
		X.append(x)
		Y.append(y)
		pos.append(np.sqrt(x**2+y**2))
	return pos
		

#creating many walks
steps,config=1000,1000
walks=np.array([walk(steps) for i in range(config)])

#mean of walks
m_walk=np.mean(walks,axis=0)

#Time scale, mean distance in log scale
log_t=np.log(range(1,steps+1))
log_r=np.log(m_walk)

#Linear fit of logarithmic vals

import numpy.polynomial.polynomial as poly
coeffs=poly.polyfit(log_t[20:],log_r[20:],1)
rfit=poly.polyval(log_t[20:],coeffs)

#for plotting

t_ext=np.insert(log_t[20:],0,0)
r_ext=np.insert(log_r[20:],0,coeffs[0])

plt.plot(log_t,log_r,'o')
plt.plot(t_ext,r_ext,'-')
plt.xlabel('log(time',fontsize=18)
plt.ylabel('log($R_{rms}$)',fontsize=18)
plt.title('2DRW')
plt.show()














		