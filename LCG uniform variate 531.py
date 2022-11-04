import matplotlib.pyplot as plt

def uvar(x):
	a,b=3,10
	x=(a+b*x)%(b-a)
	r=x/(b-a)
	return r,x

def uniform_numbers(x,size):
   L=[]
   for i in range(size):
   	r,x=uvar(x)
   	L.append(r)
   return L
   
x=(uniform_numbers(321,1000))
plt.hist(x,bins=10,ec='yellow',color='red',rwidth=0.8)
plt.show()

   