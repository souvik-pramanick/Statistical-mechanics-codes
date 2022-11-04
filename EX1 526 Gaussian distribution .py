#question1 page 526
#gaussian distributions
from numpy.random import normal
import matplotlib.pyplot as plt
x=normal(0,0.5,100000)
plt.hist(x,bins=50,ec='k',rwidth=0.8,histtype='bar')
plt.show()
