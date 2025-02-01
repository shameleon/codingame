
""" code from https://en.wikipedia.org/wiki/Chudnovsky_algorithm

"""

import decimal
import time


def binary_split(a, b):
    if b == a + 1:
        Pab = -(6*a - 5)*(2*a - 1)*(6*a - 1)
        Qab = 10939058860032000 * a**3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)
        
        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky(n):
    """Chudnovsky algorithm."""
    P1n, Q1n, R1n = binary_split(1, n)
    return (426880 * decimal.Decimal(10005).sqrt() * Q1n) / (13591409*Q1n + R1n)


#print(f"1 = {chudnovsky(2)}")  # 3.141592653589793238462643384

start = time.time()
index= 79100
n = 20
decimal.getcontext().prec = index + 10 # number of digits of decimal precision
# for n in range(2,100):
#     print(f"{n} = {chudnovsky(n)}")  # 3.14159265358979323846264338...
ans = str(chudnovsky(10))[index:index + n + 1].replace('.','')
print('time', time.time() - start)
print("\nOUTPUT")
print(ans)

"""
index= 79100
n = 20

time 2.1317319869995117

OUTPUT
97837958342
"""