import sys


class NumeralSymbols:
    def __init__(self, l, h, numeral):
        self.l = l
        self.h = h
        self.numeral = numeral
        self.base = 20
        self.d = {}
        for n in range(self.base):
            self.d[n] = [numeral[i][n * l:(n + 1) * l] for i in range(h)]

    def _mayan_digit_to_int(self, mayan):
        for key, value in self.d.items():
            to_be_found = self.h
            for i in range(self.h):
                if mayan[i] != value[i]:
                    break
                to_be_found -= 1
            if to_be_found == 0:
                return key
        return None

    def _int_to_mayan_digit(self, number):
        if 0 <= number < self.base:
            return self.d[number]
        return None
    
    def mayan_to_decimal(self, mayan):
        size = len(mayan) // self.h
        result = 0
        while size > 0:
            mayan_digit = [mayan.pop(0) for i in range(self.h)]
            nb = self._mayan_digit_to_int(mayan_digit)
            result += nb * pow(20, size - 1)
            size -= 1
        return result



class MayanOperation:
    def __init__(self, l, h, numeral):
        self.num = NumeralSymbols(l, h, numeral)

    def calculate(self, operand1, operand2, operation):
        self.nb1 = self.num.mayan_to_decimal(operand1)
        self.nb2 = self.num.mayan_to_decimal(operand2)
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
            [print(line) for line in self.num._int_to_mayan_digit(0)]
        factors = self.factorize_to_base_20(result)
        for dec in factors:
            output = self.num._int_to_mayan_digit(dec)
            for line in output:
                print(line)

    @staticmethod
    def factorize_to_base_20(dec):
        p = 8
        while dec // pow(20, p) == 0:
            p -= 1
        factors = []
        for n in range(p, -1, -1):
            factors.append(dec // pow(20, n))
            dec = dec % pow(20, n)
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
