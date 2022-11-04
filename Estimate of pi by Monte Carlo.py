#value of pi from Monte Carlo simulation

import numpy as np

X=[]

for i in range(450):
	x=np.random.uniform(-1,1,1000)
	y=np.random.uniform(-1,1,1000)
	z=(x**2+y**2)<1
	pi=4*np.sum(z)/1000
	X.append(pi)

avg_pi=sum(X)/len(X)

print('Values of pis from trials:  ')
print(X)


print('Average value of pi from Monte Carlo simulation: ',avg_pi)
	

	
	
	
