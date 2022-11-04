#EX2 526 uniform and normal distribution plots 

from numpy.random import uniform,normal
import matplotlib.pyplot as plt

x=uniform(0,1,10000)
y=normal(1,2,10000)

plt.subplot(1,2,1)
plt.hist(x,bins=50,color='yellow',ec='black',rwidth=0.8,label='Uniform plots')
plt.legend(loc='best')

plt.subplot(1,2,2)
plt.hist(y,bins=50,color='magenta',ec='black',rwidth=0.8,label='Normal plots')
plt.legend(loc='best')

plt.show()

