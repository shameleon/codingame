import sys

l , n = [int(input()) for x in range(2)]
print(l, n, file=sys.stderr, flush=True)
s = [int(i) for i in input().split()]
print(s, file=sys.stderr, flush=True)
print(l - min(min(s), l - max(s)))
