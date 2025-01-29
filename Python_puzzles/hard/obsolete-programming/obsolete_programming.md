# Obsolete Programming

# Best score

### Contribution by Zorg1
Approved by dbdr , JBM and chouch

### Goal
How is your CSB ? Very bad, in fact, and you have been moved from the prestigious Bot Division to the awful Legacy Softwares Division where you must maintain obsolete and crappy code that runs 90% of your corporation's business.

Today you must write an interpreter for a strange and forgotten language, written in a narrow character set : only uppercase letters, digits, minus sign, space and newline.

Basically the language is based on RPN (Reverse Polish Notation) with the abilty to define new instructions.

Lines are split in instructions separated by space(s).

If the instruction is a number, simply put in on top of the stack.
The operations (ADD, SUB, MUL, DIV, MOD) pop the last two numbers out of the stack and push the result back on top.
For example after, 2 5 SUB 8, the stack is -3 8.
DIV is the integer quotient and MOD the remainder of the division.

There are also operators that act on the stack itself:
POP removes the top number.
DUP duplicates the top number.
SWP swaps the two top numbers. 4 5 SWP 6 swaps 4 and 5 then pushes 6 on top, the stack is 5 4 6.
ROT brings to the top the third number of the stack. If the stack is 1 2 3 4, ROT changes it in 1 3 4 2.
OVR copies the second top number of the stack on the top. If the stack is 1 2 3 4, OVR changes it in 1 2 3 4 3.

POS removes the top number, push 1 if this number is ≥ 0, otherwise push 0.
NOT removes the top number, push 1 if this number is 0, otherwise push 0.
OUT removes the top number and print it on the standard output, followed by a newline char.

To define a new instruction the syntax is :

DEF name RPN instructions END

The instructions between DEF and END are not executed immediately but stored to be executed when name appears as instruction outside, after its definition.
name must not be an already defined instruction or a number.
Note that name can appears in its own definition (recursion is available).

For example
DEF SQ DUP MUL END defines the instruction SQ
when 4 SQ appears, 4 is pushed on the stack, then DUP then MUL are executed.

Inside a definition, conditionals are available :

IF RPN instructions FI
remove the top number, if this number is not zero, the instructions between IF and FI are executed, and continue with instructions after FI. If the number is zero, the execution continues after FI.

IF RPN instructions 1 ELS RPN instructions 2 FI
Remove the top number, if this number is not zero, the instructions between IF and ELS are executed, and continue with instructions after FI. If the number is zero, the instructions between ELS and FI are executed and continue execution after FI.

The two conditional structures can be nested.
Input
Line 1: N : number of input lines of code
N lines: Obsolete code
Output
any number of lines: whatever the obsolet program outputs
Constraints
1 ≤ N ≤ 100
All the numbers are signed integer (minimum width : 30 bits).
All tests are correct (ie don't use undefined instruction) and use MOD and DIV instructions only with positive arguments.
Example
Input

6
10 5 ADD OUT
10 5 SUB OUT
12 24 SUB OUT
30 10 MUL OUT
50 7 DIV OUT
50 7 MOD OUT

Output

15
5
-12
300
7
1

### Possibles improvements from other coders solutions :

```python
class BuiltIn:
    class Operators:
        def Add(): stack.append(stack.pop(-2) + stack.pop())


functions = { "ADD":  BuiltIn.Operators.add., }
```

#### NOT MY CODE :

Mercy38 code, using regular expressions

```Python
from functools import partial
from re import compile

D = {
    "ADD":lambda:stack.append(stack.pop() + stack.pop()),
    "SUB":lambda:stack.append(stack.pop(-2) - stack.pop()),
    "MUL":lambda:stack.append(stack.pop() * stack.pop()),
    "DIV":lambda:stack.append(stack.pop(-2) // stack.pop()),
    "MOD":lambda:stack.append(stack.pop(-2) % stack.pop()),
    "POP":lambda:stack.pop(),
    "DUP":lambda:stack.append(stack[-1]),
    "SWP":lambda:stack.append(stack.pop(-2)),
    "ROT":lambda:stack.append(stack.pop(-3)),
    "OVR":lambda:stack.append(stack[-2]),
    "POS":lambda:stack.append(int(stack.pop() >= 0)),
    "NOT":lambda:stack.append(int(stack.pop() == 0)),
    "OUT":lambda:print(stack.pop())
}

def execute(commands):
    def condition(i):
        count, inst1, inst2 = 0, None, None
        for j,y in enumerate(commands[i+1:], i+1):
            if y == "IF":
                count += 1
            elif y == "ELS" and count == 0:
                inst1 = j
            elif y == "FI":
                if count == 0:
                    if inst1:
                        inst2 = j
                    else:
                        inst1 = j
                    break
                count -= 1
        if stack.pop():
            execute(commands[i+1:inst1])
        elif inst2:
            execute(commands[inst1+1:inst2])
        return inst2 or inst1

    i = 0
    while i < len(commands):
        x = commands[i]
        try:
            stack.append(int(x))
        except ValueError:
            if x in D:
                D[x]()
            elif x in func:
                execute(func[x])
            else:
                i = condition(i)
        i += 1

stack, func = [], {}
def my_sub(x):
    name, inst = x.groups()
    func[name] = inst.split()
    return ""

REGEX = partial(compile(r"DEF (.+?) (.+?) END").sub, my_sub)
lines = ' '.join(input().strip() for _ in range(int(input())))
code = REGEX(lines).split()
execute(code)
```


Very short solution:

```python
from operator import *

OP = {'ADD':add, 'SUB':sub, 'MUL':mul, 'DIV':floordiv, 'MOD':mod}

def run(Func, S, fname='_MAIN_'):
    Prog = Func[fname]
    i = 0
    while i<len(Prog):
        I = Prog[i]
        if isinstance(I, int):
            S.append(I)
        elif isinstance(I, tuple):         # IF / ELS
            if I[0]=='ELS' or S.pop()==0:  # jump case
                i = I[1]
                continue
        elif I in OP:
            b,a = S.pop(),S.pop()
            S.append(OP[I](a,b))
        elif I=='POP':
            S.pop()
        elif I=='DUP':
            S.append(S[-1])
        elif I=='SWP':
            S[-1],S[-2] = S[-2],S[-1]
        elif I=='ROT':
            S[-3],S[-2],S[-1] = S[-2],S[-1],S[-3]
        elif I=='OVR':
            S.append(S[-2])
        elif I=='POS':
            S.append(int(S.pop()>=0))
        elif I=='NOT':
            S.append(int(S.pop()==0))
        elif I=='OUT':
            print(S.pop())
        else:
            assert I in Func
            run(Func, S, I)
        i += 1

def parse_func(Prog, Func, i=0):
    assert Prog[i]=='DEF'
    fname = Prog[i+1]
    i += 2
    Body = []
    Cond = []
    while Prog[i]!='END':
        I = Prog[i]
        if I=='DEF':
            i = parse_func(Prog, Func, i)
            continue
        elif I=='IF':
            Cond.append(len(Body))
        elif I=='ELS':
            Cond.append(len(Body))
        elif I=='FI':
            ifi = Cond.pop()
            if Body[ifi]=='ELS':
                ifi, eli = Cond.pop(), ifi
                Body[ifi] = ('IF', eli+1)
                Body[eli] = ('ELS', len(Body))
            else:
                Body[ifi] = ('IF', len(Body))
            i += 1
            continue  # we do not keep the FI token
        else:
            try:
                I = int(I)
            except ValueError:
                pass
        Body.append(I)
        i += 1
    assert fname not in Func
    Func[fname] = Body
    return i+1

def main():
    N = int(input())
    Prog = ['DEF', '_MAIN_']
    for _ in range(N):
        Prog += input().split()
    Prog.append('END')
    Func = {}
    parse_func(Prog, Func)
    run(Func, [])

main()
```


other short solution :
```python
stack = []
seq = {}

def Add():
    stack.append(stack.pop()+stack.pop())

def Sub():
    stack.append(-stack.pop()+stack.pop())

def Mul():
    stack.append(stack.pop()*stack.pop())

def Div():
    stack.append(stack.pop(-2)//stack.pop())

def Mod():
    stack.append(stack.pop(-2)%stack.pop())

def Pop():
    stack.pop()

def Dup():
    stack.append(stack[-1])

def Swp():
    stack.append(stack.pop(-2))

def Rot():
    stack.append(stack.pop(-3))

def Ovr():
    stack.append(stack[-2])

def Pos():
    stack.append(1 if stack.pop() >= 0 else 0)

def Not():
    stack.append(1 if stack.pop() == 0 else 0)

def Out():
    print(stack.pop())

def Seq():
    name = line.pop(0)
    seq[name] = []
    while True:
        inst = line.pop(0)
        if inst == "END":
            break
        seq[name].append(inst)

def If():
    global line
    instructions = []
    level = 1
    TrueFalse = stack.pop() != 0
    current = True
    while True:
        inst = line.pop(0)
        if inst == "IF":
            level += 1
        elif inst == "FI":
            if level == 1:
                break
            else:
                level -= 1
        elif inst == "ELS":
            if level == 1:
                current = False
                continue
        if TrueFalse == current:
            instructions.append(inst)
    line = instructions + line


operations = {
    "ADD": Add,
    "SUB": Sub,
    "MUL": Mul,
    "DIV": Div,
    "MOD": Mod,
    "POP": Pop,
    "DUP": Dup,
    "SWP": Swp,
    "ROT": Rot,
    "OVR": Ovr,
    "POS": Pos,
    "NOT": Not,
    "OUT": Out,
    "DEF": Seq,
    "IF": If,
}


n = int(input())

line = " ".join(input() for i in range(n)).split()
while line:
    inst = line.pop(0)
    if inst in operations:
        operations[inst]()
    elif inst in seq:
        line = seq[inst] + line
    else:
        stack.append(int(inst))
```

