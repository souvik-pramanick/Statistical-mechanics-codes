import numpy as np
import matplotlib.pyplot as plt

sample_mean=lambda n:np.mean(np.random.uniform(1,7,size=(n)))
x=[sample_mean(n=100) for i in range(10000)]
plt.hist(x)
plt.show()