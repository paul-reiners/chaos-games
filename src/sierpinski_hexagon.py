import sys

from sierpinski_n_gon import sierpinski_m_gon

if __name__ == "__main__":
    n = int(sys.argv[1])
    compression_ratio = float(sys.argv[2])
    sierpinski_m_gon(n, 6, '../img/sierpinski_hexagon.png', compression_ratio)
