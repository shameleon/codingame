import sys
import decimal
import math
import time

""" TIMEOUT for index=79100"""

def compute_pi_chudnovsky(digits):
    decimal.getcontext().prec = digits + 10
    C = 426880 * decimal.Decimal(math.sqrt(10005))
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = L

    for i in range(1, digits // 14 + 1):  # 14 décimales par itération environ
        M = (K ** 3 - 16 * K) * M // i ** 3
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12

    pi = C / S
    return str(pi)


start = time.time()
index= 79100
n = 20
decimal.getcontext().prec = index + 10 # number of digits of decimal precision
# for n in range(2,100):
#     print(f"{n} = {chudnovsky(n)}")  # 3.14159265358979323846264338...
pi_str = compute_pi_chudnovsky(index + n + 1)
pi_str = pi_str.replace('.', '')
print('time', time.time() - start)
print("\nOUTPUT")
print(pi_str[index:index + n])

"""
index= 79100
n = 20

time TIMEOUT

OUTPUT
97837958342
"""