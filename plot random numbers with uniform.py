#Random numbers from unifrom distribution

from numpy.random import uniform
import matplotlib.pyplot as plt
x=uniform(0,1,10000)
plt.plot(x)
plt.show()