import sys
m = "".join([format(ord(c), 'b').zfill(7) for c in input()])
p = ' '
for i, b in enumerate(m):
    print((' ' * (i != 0) + '0' + '0' * (b == '0') + ' 0') * (b != p) + '0' * (b == p), end='')
    p = b