#MC integration for a function(here sinx from [0,pi]

import numpy as np

N=10000 #no of random points
a,b=0,np.pi
x=np.random.uniform(a,b,N) #generation of points
f=lambda x:np.sin(x) #function

MC_value=(b-a)*np.mean(f(x))
print(MC_value)

#error
err=lambda N:np.std(f(x))/np.sqrt(N)
print(err(10000))






