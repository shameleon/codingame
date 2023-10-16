import sys
import math

""" progress 59% in Python
solved in c++
"""

class StockExchangeLosses:
    def __init__(self, n, values):
        self.n = n
        self.v = values
        # print(values, file=sys.stderr, flush=True)

    def max_decrease(self):
        """ diffs = np.diff(v)"""
        diffs = [j-i for (i,j) in zip(self.v[:-1], self.v[1:])]
        # print(diffs, file=sys.stderr, flush=True)
        losses = []
        decr = 0
        incr = 0
        start = 0
        for i, n in enumerate(diffs):
            if n < 0:
                start = i
                decr += n
            else:
                incr += n
            if decr + incr >= 0:
                # print(start, i, decr, incr, file=sys.stderr, flush=True)
                losses.append(decr)
                incr = 0
                decr = 0
        losses.append(decr + incr)
        result = min(losses)
        return result

    
def main():
    n = int(input())
    v = [int(i) for i in input().split()]
    stock = StockExchangeLosses(n, v)
    print(stock.max_decrease())


if __name__ == "__main__":
    main()
