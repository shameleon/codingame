

with open('pi.txt', "r") as file:
    lines = [line.rstrip().replace(' ','').replace('.','')  for line in file]
pi_str = ''.join(lines)
i, n = [79100, 20]
print(pi_str[i:i+n])
print(len(pi_str))