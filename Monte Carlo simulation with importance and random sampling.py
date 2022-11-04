from scipy.integrate import simps
import numpy as np


q=lambda x:(1/np.sqrt(2*np.pi))*np.exp(-(x-5)**2/2)
f=lambda x:np.exp(-2*np.abs(x-5))
p=lambda x:1/10

a,b=0,10
N=1000
x=np.random.normal(5,1,N)

y_imps=(b-a)*f(x)*p(x)/q(x) #importance sampling

y_rs=(b-a)*f(x)   #random sampling

print('importance sampling','integration: ',np.mean(y_imps),'variance: ',np.var(y_imps))

print('random sampling','integration: ',np.mean(y_rs),'variance: ',np.mean(y_rs))


