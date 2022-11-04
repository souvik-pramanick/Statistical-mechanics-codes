#Monte Carlo integration in essence algorithm

def MCint(f,a,b):   #a=lower limit, b=upper limit
	N=10000          #no. of  trials
	x=np.linspace(a,b,1001)
	ymax=1.2*max(f(x))  #height of box
	area=(b-a)*ymax #area of box
	xval=np.random.uniform(a,b,N) #random x vals
	yval=np.random.random(N)*ymax #random y vals
	under=np.sum(yval<f(xval)) #no of pts under curve
	return area*under/N
	
import numpy as np
f=lambda x:np.sin(x)  #the integrand
print(MCint(f,0,np.pi))

	
	      
	
	