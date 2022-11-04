#Maxwell Boltzmann distribution problem
#Question:
	#A system consists of two particles each of which can be in any one single particle levels of respective energies 0 and ε. The system is in contact with a heat reservoir at temperature T. The particles follow MB-Statistics. Find 
	#(i)Partition function(Z), 
	#(ii)Average energy(<E>),
	#(iii)Relative R.M.S.fluctuation in E              #(iv)Specific heat capacity at constant volume

#express energies in units of kT so take kT=1

import numpy as np
import matplotlib.pyplot as plt

#i)Finding partition function
eps=np.linspace(0,5,1001) #energies
Z=1+np.exp(-2*eps)+2*np.exp(-eps) #partition function
plt.suptitle('Boltzmann Statistics for 2body problem in two energy states')
plt.subplot(2,2,1)
plt.plot(eps,Z,'o-',c='red',label='Partition function')
plt.legend(loc='best')
plt.xlim(0,2)


#ii)Finding average energy
avg_energy=(2*eps*np.exp(-2*eps)+2*eps*np.exp(-eps))/Z
plt.subplot(2,2,2)
plt.plot(eps,avg_energy,'o-',c='blue',label='Average energy')
plt.legend(loc='best')
plt.xlim(0,5)
plt.xlabel('Particle energy',fontsize=10)
plt.ylabel('Average energy',fontsize=10)



#iii)Relative RMS fluctuation in E
rel_rms=np.sqrt(Z*(2*np.exp(-2*eps)+np.exp(-eps))/2)/(np.exp(-2*eps)+np.exp(-eps))
plt.subplot(2,2,3)
plt.plot(eps,rel_rms,c='green',label='Relative RMS')
plt.legend(loc='best')
plt.xlim(0,5)
plt.xlabel('Particle energy',fontsize=10)
plt.ylabel('Relative RMS energy',fontsize=10)

#iv)Cv
energy=1 #arbitrary unit
T=np.linspace(0.1,2,100)
Z=1+np.exp(-2/T)+2*np.exp(-1/T)
energy_av=2*(np.exp(-2/T)+np.exp(-1/T))/Z
sqav_energy=2*(2*np.exp(-2/T)+np.exp(-1/T))/Z
CV=(sqav_energy-energy_av**2)/T**2
plt.subplot(2,2,4)
plt.plot(T,CV,'o-',c='orange',label='Specific heat')
plt.legend(loc='best')
plt.xlim(0,2)
plt.xlabel('Temperature')
plt.ylabel('Specific heat')
plt.show()




	