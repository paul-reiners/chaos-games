import math
import random

import matplotlib.pyplot as plt


def ifsp(attractors, n, fig_path):
    def w(x, attractor):
        compression_ratio = attractor['compression_ratio']
        return [compression_ratio * x[i] + (1.0 - compression_ratio) * attractor['point'][i] for i in range(2)]

    xs = [0.0] * n
    ys = [0.0] * n
    x = attractors[0]['point']
    m = len(attractors)
    for i in range(n):
        xs[i] = x[0]
        ys[i] = x[1]
        prob_sum = 0.0
        attractor_index = None
        r = random.random()
        for i in range(m):
            prob_sum += attractors[i]['probability']
            if prob_sum >= r:
                if prob_sum > r:
                    attractor_index = i - 1
                else:
                    attractor_index = i

                break
        x = w(x, attractors[attractor_index])
    plt.scatter(xs[20:], ys[20:], 1)
    plt.savefig(fig_path)
    plt.show()
