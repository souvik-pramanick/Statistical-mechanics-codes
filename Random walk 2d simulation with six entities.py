

import numpy as np
import matplotlib.pyplot as plt

def real_time_random_walk_2D_NT(
    nb_steps, nb_trajs, with_dots=False, save_trajs=False, tpause=.01
    ):
 
    skoki = np.array([[0, 1], [1, 0], [-1, 0], [0, -1]])
    trajs = np.zeros((nb_trajs, 1, 2))
    for i in range(nb_steps):
        _steps = []
        for j in range(nb_trajs):
            traj = trajs[j,:,:]
            losy = np.random.randint(4, size = 1)
            temp = skoki[losy, :]
            traj = np.concatenate((traj, temp), axis = 0)
            traj[-1,:]   += traj[-2,:]
            _steps.append(traj)
        if save_trajs or with_dots:
            trajs = np.array(_steps)
            if with_dots:
                plt.cla()
                plt.plot(trajs[:,i, 0].T, trajs[:,i, 1].T, 'ro') 
                plt.plot(trajs[:,:i+1, 0].T, trajs[:,:i+1, 1].T)
            else:
                plt.plot(trajs[:,-1+i:i+1, 0].T, trajs[:,-1+i:i+1, 1].T)
        else:
            trajs = np.array(_steps)[:,-2:,:]
            plt.plot(trajs[:,:, 0].T, trajs[:,:, 1].T)

        plt.pause(tpause)


real_time_random_walk_2D_NT(1000, 6, with_dots=True)