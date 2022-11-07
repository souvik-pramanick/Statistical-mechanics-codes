import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import animation

def random_walk(input):
    r = np.random.uniform(0,1,1)
    if r <=0.33:
        z = 1
    elif r > 0.33 and r <=0.66:
        z = 0
    else:
        z = -1
    return input + z

def animate(i):
    global rw_array,z,T
    z = random_walk(z)
    rw_array.append(z)
    line.set_data(np.arange(len(rw_array)),np.array(rw_array))
    if len(rw_array) >= T:
        T = T * 2
        plt.xlim(0,T)
    return line,

def init():
    line.set_data([],[])
    return line,

T = 100
rw_array=[]
z = 0

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.ylim(-50,50)
plt.xlim(0,T)
plt.xlabel('t')
plt.title('Simple Random Walk')
line, = ax.plot([],[],lw=2)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)
plt.show()