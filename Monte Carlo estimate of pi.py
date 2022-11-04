########################
#Name:SOUVIK PRAMANICK
#Semester:5
#Subject:Physics(Hons.)
#Registration no.:
#Roll no.:
########################
#
#Monte Carlo estimate of pi
#
########################
#CODE:
import numpy as np
x=np.random.uniform(-1,1,1000)
y=np.random.uniform(-1,1,1000)
z=x**2+y**2<1   #array contains boolean true and false
pi=4*sum(z)/1000  #sum(z) is sum of True=1 and False=0
print('pi = ',pi)

########################