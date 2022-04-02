import math
import random
import sys
from itertools import permutations

import matplotlib.pyplot as plt

def main(n):
    indices = [0, 1, 2, 3, 4, 5]
    v = [[math.sin(indices[i] * 2.0 * math.pi / 6), math.cos(indices[i] * 2.0 * math.pi / 6)] for i in range(6)]

    def w(x, j):
        return [(x[i] + 5 * v[j][i]) / 6.0 for i in range(2)]

    xs = [0.0] * n
    ys = [0.0] * n
    x = v[0]
    for i in range(n):
        xs[i] = x[0]
        ys[i] = x[1]
        r = random.randint(0, 5)
        x = w(x, r)
    plt.scatter(xs[4:], ys[4:], 1)
    plt.savefig('../img/sierpinski_hexagon.png')
    plt.show()

if __name__ == "__main__":
    n = int(sys.argv[1])
    main(n)
