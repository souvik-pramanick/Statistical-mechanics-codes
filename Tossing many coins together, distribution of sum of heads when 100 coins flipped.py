#tossing of many coins together

import numpy as np
import matplotlib.pyplot as plt

n,trials=100,10000

f=[sum(np.random.randint(0,2,size=n)) for i in range(trials)]

x,y=np.unique(f, return_counts=True)
y=y/np.max(y)

plt.plot(x,y,'o')
plt.xlabel('No of heads')
plt.show()