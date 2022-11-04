#using LCG to generate uniform variate


import numpy as np
import matplotlib.pyplot as plt

def uvar(x):
	m,a,c=1771875,2416,374441
	x=(a*x+c)%m
	r=x/m
	return r,x

def uniform_numbers(x,size):
	L=[]
	for i in range(size):
		r,x=uvar(x)
		L.append(r)
	return L
	
x=uniform_numbers(234567,10000)
plt.hist(x,bins=10,ec='k',color='yellow',rwidth=0.8)
plt.show()