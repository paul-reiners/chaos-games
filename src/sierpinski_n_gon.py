import math
import random

import matplotlib.pyplot as plt


def sierpinski_m_gon(n, m, fig_path, compression_ratio):
    v = [[math.sin(i * math.pi / 3.0), math.cos(i * math.pi / 3.0)] for i in range(m)]

    def w(x, j):
        return [compression_ratio * x[i] + (1.0 - compression_ratio) * v[j][i] for i in range(2)]

    xs = [0.0] * n
    ys = [0.0] * n
    x = v[0]
    for i in range(n):
        xs[i] = x[0]
        ys[i] = x[1]
        r = random.randint(0, m - 1)
        x = w(x, r)
    plt.scatter(xs[20:], ys[20:], 1)
    plt.savefig(fig_path)
    plt.show()
