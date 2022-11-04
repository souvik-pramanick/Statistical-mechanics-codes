#i)Create 100 uniform random numbers between 0 and 1. 
#ii)Find the standard deviation of the numbers created.
#iii)Find how many numbers are less than 0.5 and how many are greater than it.

#Exercise1 572

import numpy as np

#calculation of standard deviation
x=np.random.random(100)
SD=np.std(x)
print('Array of random floats')
print(x)
print('STANDARD DEVIATION:  ',SD)

less_counts=0
more_counts=0

for i in x:
	if i<0.5:
		less_counts=less_counts+1  #less 0.5 counts
	else:
		more_counts=more_counts+1 #great 0.5 counts

print('Numbers lesser than 0.5:  ', less_counts)
print('Numbers greater than 0.5:  ',more_counts)
		

