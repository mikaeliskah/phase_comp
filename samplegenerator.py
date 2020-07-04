# this module generates sample data
import numpy as np


def sin_sample(t):
    r = np.random.random()
    sample = np.sin(2*np.pi*1*t) + r
    return sample
