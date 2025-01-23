
# Stunning numbers

### Best score
100

### author
A contribution by VilBoub
Approved by Antsurf , jddingemanse and FredericLocquet

### Goal

When written with digits, some digits may still read when flipped (0, 1, 2, 5, 6, 8, and 9) while others mean nothing when flipped (3, 4, and 7).
Once flipped, some integers remain identical like 69, they are called "stunning numbers"!
Given an integer n, say whether it is "stunning" or not, then find the next "stunning number"...

 --          --    --          --    --    --    --    --
|  |     |     |     |  |  |  |     |        |  |  |  |  |
             --    --    --    --    --          --    --
|  |     |  |        |     |     |  |  |     |  |  |     |
 --          --    --          --    --          --    --


 --    --          --    --          --    --          --
|     |  |  |     |  |  |     |     |        |  |     |  |
 --    --          --    --    --    --    --        
|  |  |  |  |        |     |  |  |  |     |     |     |  |
 --    --    --    --    --          --    --          --


Even if the number 1 is a little off once flipped, it is considered stunning.
Input
n an integer
Output
Line 1: true if n is a "stunning number", false otherwise
Line 2: the next "stunning number".
Constraints
0 <= n <= 10^20
Example
Input

69

Output

true
88


### Best Solutions by others - NOT MY CODE

```python
n = list(map(int, list(nStr:=input())))
d = {0:0, 1:1, 2:2, 5:5, 6:9, 8:8, 9:6}
print(str(all(x in d and d[x]==y for x,y in zip(n, n[::-1]))).lower())

digits, extra = len(nStr), 0
left = n[:(digits+1)//2]
while 1:
    zeroAll = 0
    for i in range(len(left)):
        if zeroAll: left[i] = 0
        else:
            while left[i] in {3,4,7}:
                left[i] += 1
                zeroAll = 1
    next = left + [d[c] for c in left[::-1][(digits+extra)%2::]]
    nextStr = "".join(str(x) for x in next)
    if (len(nextStr)%2==0 or nextStr[len(nextStr)//2] in "01258") and int(nextStr) > int(nStr):
        exit(print(nextStr))
    n1 = n2 = int(nextStr[:(len(nextStr)+1)//2])
    while 1:
        n2 += 1
        lastDigit, extra = n2%10, len(str(n2)) > len(str(n1))
        if lastDigit in {0,1,2,5,8} or (lastDigit in {6,9} and (digits+extra+1)%2):
            left = list(map(int, list(str(n2))))[:[len(str(n2)), -1][digits%2 and extra==1]]
            break
```

```python
import sys
d={"1":"1", "2":"2", "0":"0", "5":"5", "6":"9", "9":"6", "8":"8"}
def isok(c):
    if any(e in "347" for e in c):
        return False
    else:
        s=""
        for e in reversed(c):
            s+=d[e]
        return c==s


n = input()
print(str(isok(n)).lower())
n=str(int(n)+1)

if len(n)>7 and len(n)%2==1:
    m = n[:len(n)//2 +1]
    while any(e in "347" for e in m) or m[-1] not in "0125":
        m=str(int(m)+1)
    s = m
    for e in m[:-1][::-1]:
        s+=d[e]
    print(s)
elif len(n)>8 and len(n)%2==0:
    m = n[:len(n)//2]
    while any(e in "347" for e in m):
        m=str(int(m)+1)
    s = m
    for e in m[::-1]:
        s+=d[e]
    print(s)
else:
    if n[0]in"34":n="5"+"0"*(len(n)-1)
    if n[0]=="7":n="8"+"0"*(len(n)-1)
    while not isok(n):
        n=str(int(n)+1)
    print(n)
```

