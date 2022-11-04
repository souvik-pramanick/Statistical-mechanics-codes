#simulation of coin tossing

import matplotlib.pyplot as plt
import numpy as np

n=100000  #number of trials

N=range(1,10000)
x=np.random.choice([0,1],size=(n)) #array of 0's and 1's
y=[np.sum(x[:i])/i for i in N]


plt.plot(N,y)
plt.title('Fraction of heads')


plt.show()





