import math
import sys

from integrated_function_system_probabilities import ifsp

v_1 = [-1.0, 0.0]
v_2 = [1.0, 0.0]
v_3 = [0.0, math.sqrt(3.0)]
vs = [v_1, v_2, v_3]


def main(n):
    attractors = [{'point': vs[i], 'compression_ratio': 0.5, 'probability': 1.0 / 3.0} for i in range(3)]
    fig_path = '../img/sierpinski_triangle.png'
    ifsp(attractors, n, fig_path)


if __name__ == "__main__":
    n = int(sys.argv[1])
    main(n)
