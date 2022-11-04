import numpy as np
import matplotlib.pyplot as plt

N=10000
x=np.random.uniform(0,1,10000)
x_avg=np.mean(x)


c=lambda k:np.mean([(x[i]-x_avg)*(x[i+k]-x_avg) for i in range(N-k)])

r=lambda k:c(k)/c(0)

corr=[r(k) for k in range(1000)]

fig,ax1=plt.subplots()
ax1.set_title('Autocorrelation plot')

left,bottom,width,height=0.35,0.3,0.5,0.5

ax2=fig.add_axes([left,bottom,width,height])

ax1.plot(corr)
ax2.plot(range(200,1000),corr[200:])

plt.show()


