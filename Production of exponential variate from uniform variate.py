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
	
x=expo_nos(12379,100000)
plt.hist(x,bins=50,color='k',edgecolor='w')
plt.show()
   