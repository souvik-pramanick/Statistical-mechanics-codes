import numpy as np  
import matplotlib.pyplot as plt  
newparams = {'axes.labelsize': 10, 'axes.linewidth': 1.5, 'savefig.dpi':   
    300,   
    'lines.linewidth': 2, 'figure.figsize': (12, 10),    
    'legend.frameon': True,   
    'legend.handlelength': 0.7}   
plt.rcParams.update(newparams)   
E = np.linspace(-0.5,0.5,1001) #energy range  
e = 1.6e-19 #electric charge  
k = 1.38e-23 #Boltzmann constant(joule per kelvin)  
u = 0 # considering chemeical potential of the substance is zero  
def Fn(T,a):
       return 1/((np.exp(((E-u)*e)/(k*T)))+a)  
 
plt.suptitle("Plot of the following functions at different temperatures",size=16,color='b',fontstyle ="italic")  
plt.subplot(2,2,1)  
plt.plot(E,Fn(100,0),label='T = 100 K')  
plt.plot(E,Fn(300,0),label='T = 300 K')  
plt.plot(E,Fn(500,0),label='T = 500 K')  
plt.plot(E,Fn(700,0),label='T = 700 K')  
plt.ylim(0,3)  
plt.xlabel('Energy(eV)')  
plt.ylabel('f(E)')  
plt.legend(loc='best',prop={'size':12})  
plt.title("Maxwell-Boltzmann distribution for u=0")  
plt.subplot(2,2,2)  
plt.plot(E,Fn(100,-1),label='T = 100 K')  
plt.plot(E,Fn(300,-1),label='T = 300 K')  
plt.plot(E,Fn(500,-1),label='T = 500 K')  
plt.plot(E,Fn(700,-1),label='T = 700 K')  
plt.xlim(0,1)  
plt.ylim(0,2)  
plt.xlabel('Energy(eV)')  
plt.ylabel('f(E)')  
plt.legend(loc='best',prop={'size':12})        
plt.title("Bose-Einstein distribution for u=0")  
plt.subplot(2,2,3)  
plt.plot(E,Fn(100,+1),label='T = 100 K')  
plt.plot(E,Fn(300,+1),label='T = 300 K')  
plt.plot(E,Fn(500,+1),label='T = 500 K')  
plt.plot(E,Fn(700,+1),label='T = 700 K')  
plt.legend(loc='best',prop={'size':12})  
plt.ylim(0,1)  
plt.xlabel('Energy(eV)')  
plt.ylabel('f(E)')  
plt.title("Fermi-Dirac distribution for u=0")  
plt.subplot(2,2,4)  
plt.plot(E,Fn(500,0),label='M-B distribution')  
plt.plot(E,Fn(500,-1),label='B-E distribution')  
plt.plot(E,Fn(500,+1),label='F-D distribution')  
plt.legend(loc='best',prop={'size':12})  
plt.ylim(0,4)  
plt.xlabel('Energy(eV)')  
plt.ylabel('f(E)')  
plt.title("Temperature = 500 K")  

plt.subplots_adjust(left=0.1,  
           bottom=0.1,   
           right=0.9,   
           top=0.9,   
           wspace=0.4,   
           hspace=0.4)  
plt.show()     