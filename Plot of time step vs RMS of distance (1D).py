#Plot of r.m.s. value of end to end distance as a function of time step

import numpy as np
import matplotlib.pyplot as plt

#creation of walks
N,T=10000,1000 #no of walks, time steps
t=range(1,T+1)

walks=np.random.choice([-1,1],size=(N,T))

#calc of avg
pos=np.cumsum(walks,axis=1) #along each row
pos_sq=pos**2
mean_pos_sq=np.mean(pos_sq,axis=0) #along each column
rms=np.sqrt(mean_pos_sq)

#plotting of rms as function of time
plt.suptitle('rms value of end2end distance as a function of time')
plt.subplot(1,2,1)
plt.plot(t,rms,label='t vs rms')
plt.legend(loc='best')
plt.xlabel('Time steps')
plt.ylabel('R($_{rms}$)')

#fitting and finding of exponent
t=np.log(t)
rms=np.log(rms)

import numpy.polynomial.polynomial as poly
coeffs=poly.polyfit(t,rms,1)
rmsfit=poly.polyval(t,coeffs)

#plotting in logscale with fitting
plt.subplot(1,2,2)
plt.plot(t[::10],rms[::10],'o')
plt.plot(t,rmsfit,'-',label='logscale plot')
plt.legend(loc='best')
plt.xlabel('log(time)')
plt.ylabel('log($R_{rms}$)')
plt.show()