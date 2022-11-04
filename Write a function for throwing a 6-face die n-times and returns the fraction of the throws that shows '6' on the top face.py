#Write a function for throwing a 6-face die n-times and returns the fraction of the throws that shows '6' on the top face.

import numpy as np
def die(n):
	counts=0
	x=np.random.randint(1,7,size=n)
	for i in x:
			if i==6:
				counts=counts+1
			else:
				counts=counts+0
	return x,counts/n

print('The sample space:  ',die(100)[0],'      Fraction of the throws that shows 6 on the top face:  ',die(100)[1])
				
				
			
			
			
			
	
	
	