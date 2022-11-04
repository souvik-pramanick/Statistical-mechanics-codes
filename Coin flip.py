import numpy as np
import random
import matplotlib.pyplot as plt
N=100 ## number of events
H=0
T=0
x=[]
for i in range(N):
    result = random.uniform(-1.0,1.0)
    x.append(result)
    if result<= 0.0 :
        H += 1
    else:
        T += 1
plt.hist(x,2,ec='black')
plt.title("N=%i,H=%.3f,T=%.3f"%(N,(H*1.0)/N,(T*1.0)/N))
plt.savefig("C_F.png")
plt.show()