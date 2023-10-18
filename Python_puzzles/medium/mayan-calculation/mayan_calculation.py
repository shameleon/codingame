import sys
import math

"""
progress 83%
class Numeral:
    def __init__(self, l, h, numeral):
        self.l = l
        self.h = h
        self.numeral = numeral

        for line in numeral:
            for j in range(20):
                k = j * self.l
                line[k:k+4]
"""


class Numeral:
    def __init__(self, l, h, numeral):
        self.l = l
        self.h = h
        self.numeral = numeral
        self.high = '....o...oo..ooo.oooo'
        self.lows = '....____'

    def numeral_to_dec(self, num):
        result = 0
        sections = len(num) // self.h
        for i in range(sections):
            k = i * self.h
            mayan = [num[i] for i in range(k, k + self.h)]
            dec = self._mayan_to_dec(mayan)
            print(i, mayan, dec, file=sys.stderr, flush=True)
            if dec >= 0:
                result += dec * pow(20, sections - i - 1)
        print(result, file=sys.stderr, flush=True)
        return result

    def _mayan_to_dec(self, mayan):
        pos = 0
        for i in range(self.h):
            pos += self.numeral[i].find(mayan[i])
            if pos == 0:
                return pos
        pos = self.high.find(mayan[0])
        if pos == -1:
            return pos
        nb = pos // 4
        for i in range(1, self.h):
            nb +=  5 * (self.lows.find(mayan[i]) // self.h)
            if pos == -1:
                return pos
        return nb

    def _dec_to_mayan(self, dec):
        high = ['....', 'o...', 'oo..', 'ooo.', 'oooo']
        lows = ['....', '____']
        if dec == 0:
            mayan = ['.oo.', 'o..o', '.oo.', '....']
        else:
            mayan = []
            mayan.append(high[dec % 5])
            for i in range(1, self.h):
                mayan.append(lows[dec >= 5 * i])
        return mayan


class MayanOperation:
    def __init__(self, l, h, numeral):
        self.num = Numeral(l, h, numeral)

    def calculate(self, operand1, operand2, operation):
        self.nb1 = self.num.numeral_to_dec(operand1)
        self.nb2 = self.num.numeral_to_dec(operand2)
        print(self.nb1, operation, self.nb2, file=sys.stderr, flush=True)
        result = self._operate(operation)
        self._result_to_mayan(result)

    def _operate(self, operation):
        result = self.nb1
        if operation == '+':
            result += self.nb2
        elif operation == '*':
            result *= self.nb2
        elif operation == '-':
            result -= self.nb2
        elif operation == '/' and self.nb2 != 0:
            result //= self.nb2
        return result

    def _result_to_mayan(self, result):
        print(result, file=sys.stderr, flush=True)
        if result == 0:
            [print(line) for line in  self.num._dec_to_mayan(result)]
        factors = self.factorize_to_base_20(result)
        for dec in factors:
            numeral = self.num._dec_to_mayan(dec)
            [print(line) for line in numeral]
        #if res[-1] == 0:
        #    [print(line) for line in self.num.dec_to_mayan(res[0])]

    @staticmethod
    def factorize_to_base_20(dec):
        p = 8
        while dec // pow(20, p) == 0:
            p -= 1
        factors = []
        for n in range(p, -1, -1):
            factors.append(dec // pow(20, n))
            dec = dec % pow(20, n)
        print("F", factors, file=sys.stderr, flush=True)
        return factors


def main():
    l, h = [int(i) for i in input().split()]
    print(l, h, file=sys.stderr, flush=True)
    numeral = [input() for i in range(h)]
    print(numeral, file=sys.stderr, flush=True)
    s1 = int(input())
    print(s1, file=sys.stderr, flush=True)
    mayan1 = [input() for i in range(s1)]
    print(mayan1, file=sys.stderr, flush=True)
    s2 = int(input())
    print(s1, file=sys.stderr, flush=True)
    mayan2 = [input() for i in range(s2)]
    print(mayan2, file=sys.stderr, flush=True)
    operation = input()
    print(operation, file=sys.stderr, flush=True)
    mayan_op = MayanOperation(l, h, numeral)
    mayan_op.calculate(mayan1, mayan2, operation)


if __name__ == "__main__":
    main()
