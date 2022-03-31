import math
import random
import sys

import matplotlib.pyplot as plt

v_1 = [-1.0, 0.0]
v_2 = [1.0, 0.0]
v_3 = [0.0, math.sqrt(3.0)]

def w_1(x):
    return [(x[i] + v_1[i]) / 2.0 for i in range(2)]

def w_2(x):
    return [(x[i] + v_2[i]) / 2.0 for i in range(2)]

def w_3(x):
    return [(x[i] + v_3[i]) / 2.0 for i in range(2)]

def main(n):
    plt.xlim([-1.0, 1.0])
    plt.ylim([0.0, 1.75])
    xs = [0.0] * n
    ys = [0.0] * n
    x = v_1
    for i in range(n):
        xs[i] = x[0]
        ys[i] = x[1]
        r = random.random()
        if r < 1.0 / 3.0:
            x = w_1(x)
        elif r < 2.0 / 3.0:
            x = w_2(x)
        else:
            x = w_3(x)
    plt.scatter(xs, ys)
    plt.savefig('../img/sierpinski_triangle.png')
    plt.show()

if __name__ == "__main__":
    n = int(sys.argv[1])
    main(n)
