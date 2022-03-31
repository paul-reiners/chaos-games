from numpy.linalg import inv
import random
import sys
import numpy as np

import matplotlib.pyplot as plt

M = np.array([[1., 1.], [-1., 1.]])
M_inv = inv(M)
d_0 = np.array([0., 0.])
d_1 = np.array([1., 0.])

def w_1(x):
    return np.matmul(M_inv, np.add(x, d_0))

def w_2(x):
    return np.matmul(M_inv, np.add(x, d_1))

def main(n):
    # plt.xlim([-1.0, 1.0])
    # plt.ylim([0.0, 1.75])
    xs = [0.0] * n
    ys = [0.0] * n
    x = d_0
    for i in range(n):
        xs[i] = x[0]
        ys[i] = x[1]
        r = random.random()
        if r < 0.5:
            x = w_1(x)
        else:
            x = w_2(x)
    plt.scatter(xs, ys)
    plt.savefig('../img/twin_dragon.png')
    plt.show()

if __name__ == "__main__":
    n = int(sys.argv[1])
    main(n)
