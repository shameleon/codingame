import sys


n = int(input())
nb_stacks = 30
for i in range(n):
    line = list(input())
    print(''.join(line), file=sys.stderr, flush=True)
    s = [[] for i in range(nb_stacks)]
    while line:
        c = line.pop(0)
        i = 0
        load = True
        while load:
            if len(s[i]) == 0 or ord(c) <= ord(s[i][-1]):
                s[i].append(c)
                load = False
            else:
                i += 1
    for i in range(nb_stacks):
        if len(s[i]) == 0:
            break
        # print(''.join(s[i]), file=sys.stderr, flush=True)
    print(i)