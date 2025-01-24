import sys
import numpy as np

"""100 % success"""

def main():
    n = int(input())
    xs = []
    ys = []
    xs_min = np.inf
    xs_max = -np.inf
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        if x < xs_min:
            xs_min = x
        if x > xs_max:
            xs_max = x
        xs.append(x)
        ys.append(y)
    horizontal_cable = abs(xs_min - xs_max)
    y_median = round(np.median(ys))
    vertical_cables = np.sum(np.abs(np.add(np.array(ys), - y_median)))
    print(horizontal_cable + vertical_cables)


if __name__ == '__main__':
    sys.exit(main())
