import math

from integrated_function_system_probabilities import ifsp


def sierpinski_m_gon(n, m, fig_path, compression_ratio):
    v = [[math.sin(i * math.pi / 3.0), math.cos(i * math.pi / 3.0)] for i in range(m)]
    attractors = [{'point': v[i], 'compression_ratio': compression_ratio, 'probability': 1.0 / m} for i in range(m)]
    ifsp(attractors, n, fig_path)
