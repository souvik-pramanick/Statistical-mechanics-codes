import numpy as np
import matplotlib.pyplot as plt
def Randomwalk1D(n): #n here is the no. of steps that we require
   x = 0
   y = 0
   xposition = [0] #starting from origin (0,0)
   yposition = [0] 
   for i in range (1,n+1):
       step = np.random.uniform(0,1)
       if step < 0.5: # if step is less than 0.5 we move up    
           x += 1
           y += 1  #moving up in u direction
       if step > 0.5: # if step is greater than 0.5 we move down  
           x += 1
           y += -1 #moving down in y direction
 
       xposition.append(x)
       yposition.append(y)
   return [xposition,yposition]
Randwalk = Randomwalk1D(100)
Randwalk1 = Randomwalk1D(100)
plt.plot(Randwalk[0],Randwalk[1],Randwalk1[0],Randwalk1[1],'r-', label = "Randwalk1D") 
plt.title("1-D Random Walks")
plt.show()