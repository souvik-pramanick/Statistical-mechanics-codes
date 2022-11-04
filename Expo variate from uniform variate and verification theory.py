import matplotlib.pyplot as plt
import numpy as np

def uvar(x):
	m,a,c=1771875,2416,374441
	x=(a*x+c)%m
	r=x/m
	return r,x



   
def exvar(x):
	r,x=uvar(x)
	if r!=0: rlog=-np.log(r)
	return rlog,x
	
def expo_nos(x,size):
	L=[]
	for i in range(size):
		rr,x=exvar(x)
		L.append(rr)
	return L
size=100000	
x=expo_nos(12379,100000)
p=plt.hist(x,bins=50,color='k',edgecolor='w')

freq,bins=p[0],p[1]
bin_mid=0.5*(bins[:-1]+bins[1:])
bin_width=bins[1]-bins[0]
freq_theory=size*np.exp(-bin_mid)*bin_width
plt.plot(bin_mid,freq,'o',c='k')
plt.plot(bin_mid,freq_theory,c='k')
plt.hist(x,bins=50,color='k',edgecolor='w')
plt.show()
   