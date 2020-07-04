# ToDo: GIT THIS STUFF

import samplegenerator as sg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import kalmanfilter as kf

style.use('dark_background')
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)


ys = []  # original data
est = []
err = []
est_prev = [1]
err_est_prev = [0.5]
dt = 0.1


def animate(i):
    print(i)
    # generate noisy sine sample with thrend
    sample = sg.sin_sample(i/10)+(i/100)
    # append to original data list
    ys.append(sample)
    # filter data
    (f_est, f_err) = kf.filter(ys[i], est_prev[i], err_est_prev[i], 0.5)
    # update estimate and error lists
    est.append(f_est)
    err.append(f_err)
    # print info
    print("Estimate: {0}   Error: {1}".format(est[i], err[i]))
    # update 'previous'-values for next iteration
    est_prev.append(est[i])
    err_est_prev.append(err[i])
    # plot stuff
    ax1.clear()
    ax2.clear()

    ax1.plot(ys, label='oiginal data')
    ax1.plot(est, label='estimate')
    ax2.plot(err, label='error')
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')

    ax1.set_ylabel('amplitude')
    # ax2.set_ylabel('amplitude')
    ax2.set_xlabel('time [s]')


# set figure to be animated, call animate function and set interval [ms]
ani = FuncAnimation(fig, animate, interval=100)

plt.show()
# plt.tight_layout()
