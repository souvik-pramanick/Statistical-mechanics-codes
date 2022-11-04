#Use python random number generator to estimate π up to 4 decimal points accurately

from numpy.random import uniform as u
n=1000    #number of trials
inside=sum(u(-1,1,n)**2+u(-1,1,n)**2 <=1)
pi=4*inside/n
print('%.4f'%pi)
 

