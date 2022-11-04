import numpy as np
import matplotlib.pyplot as plt

f=lambda n:[sum(np.random.randint(2,size=(n))) for i in range(trial)]

n,trial=20,10000
N,Y=[],[]

for i in range(10):
	x,y=np.unique(f(n),return_counts=True)
	x=x/n
	p=y/trial
	d=np.sqrt(sum(x*x*p)-(sum(x*p))**2)
	Y.append(d)
	N.append(n)
	n=n*2

fit=np.array(N)**(-0.5)
plt.loglog(N,Y,'o',N,fit,'-',lw=2)
plt.xlabel('Sample size')
plt.ylabel('Width')
plt.show()

	
	