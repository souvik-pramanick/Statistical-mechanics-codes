import numpy as np
import matplotlib.pyplot as plt

xpoints1=np.random.randint(25,size=(25))
ypoints1=np.random.randint(25,size=(25))

xpoints2=np.random.randint(25,size=(25))
ypoints2=np.random.randint(25,size=(25))

print('x1: ',xpoints1)
print('y1 :',ypoints1)
print('x2 :',xpoints2)
print('y2 :',ypoints2)

distances=[((xpoints2[i]-xpoints1[i])**2+(ypoints2[i]-ypoints1[i])**2)**0.5 for i in range(25)]

print('distances  :',distances)
maximum=np.max(distances)
minimum=np.min(distances)
print('maximum distance:',maximum,'minimum distance:',minimum)
print('Standard deviation :',np.std(distances))

plt.subplot(1,2,1)
with plt.xkcd():
	plt.hist(distances,bins=10,color='red',ec='black')


#next part
xpointsa=np.random.randint(25,size=(1000))
ypointsa=np.random.randint(25,size=(1000))

xpointsb=np.random.randint(25,size=(1000))
ypointsb=np.random.randint(25,size=(1000))

print('x1: ',xpointsa)
print('y1 :',ypointsa)
print('x2 :',xpointsb)
print('y2 :',ypointsb)

distances1=[((xpointsb[i]-xpointsa
[i])**2+(ypointsb[i]-ypointsa[i])**2)**0.5 for i in range(999)]

print('distances1 :',distances1)
maximum1=np.max(distances1)
minimum1=np.min(distances1)
print('maximum distance1:',maximum1,'minimum distance1:',minimum1)
print('Standard deviation1 :',np.std(distances1))
distancezero=[((xpointsb[i])**2+(ypointsb[i])**2)**0.5 for i in range(999)]


print('Mean square displacement: ',(np.mean(distancezero))**2)
plt.subplot(1,2,2)
with plt.xkcd():
	plt.hist(distances1,bins=10,color='black',ec='yellow')
	
plt.show()


