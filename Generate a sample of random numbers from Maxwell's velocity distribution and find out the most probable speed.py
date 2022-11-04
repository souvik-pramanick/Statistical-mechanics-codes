#Q Generate a sample of random numbers from Maxwell's velocity distribution and find out the most probable speed

from scipy.stats import maxwell
import numpy as np
import matplotlib.pyplot as plt


n=1000000           #no. of values
x=maxwell.rvs(loc=0,scale=1,size=n)
with plt.xkcd():
	y=plt.hist(x,bins=40,ec='red',color='black')
	plt.xlim(0,4)
	
	
freq,bins=y[0],y[1]
bin_mid=(bins[:-1]+bins[1:])/2
plt.plot(bin_mid,freq,'-o',c='Magenta')

freq_max=np.max(freq)
index=np.where(freq_max)
most_prob_speed=bin_mid[index]
plt.scatter(bin_mid[10],freq_max,s=200,label='most probable speed')
plt.legend(loc='best')
plt.title('Generation of distribution from velocity variate(MB) ')
plt.show()
	


