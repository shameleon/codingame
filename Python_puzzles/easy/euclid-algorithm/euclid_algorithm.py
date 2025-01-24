import sys


class GCD:
    def __init__(self, input_line):
        a, b = [int(i) for i in input_line.split()]
        print(a, b, file=sys.stderr, flush=True)
        gcd = calculate_gcd(a, b)
        print(f'GCD({a},{b})={gcd}')


def calculate_gcd(a: int, b: int):
    if b == 0:
        return a
    print(f'{a}={b}*{a//b}+{a%b}')
    return calculate_gcd(b, a % b)


def main():
    gcd = GCD(input())

if __name__ == '__main__':
    sys.exit(main())


