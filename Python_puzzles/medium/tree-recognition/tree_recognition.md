# Tree recogniton

[tree recognition, medium difficulty problem from CodinGame](https://www.codingame.com/ide/puzzle/tree-recognition)

A contribution by java_coffee_cup
Approved by Eulero314 , ajaiy and TBali

### My score : 100

### subject

#### Goal
Computers are becoming so advanced that they can recognize facial images, fingerprints and car license plates. Can they also recognize tree diagrams?

#### Prerequisite

Binary Search Tree (BST) is a data structure used in computer science for organizing and storing data in a sorted manner. By attempting this "not-too-easy" puzzle, you are assumed to have at least a basic understanding of BST. Concise introduction and simple BST examples will be given but it is far from being a textbook. Anyone who needs more assistance should review it from external resources before coming back to take the challenge.

Reference: https://en.wikipedia.org/wiki/Binary_search_tree

Build trees, draw diagrams

Some lists of integers, each containing unique values within the list, are given. Use each list to build a binary search tree. Use the first integer in the list as the root node. Successively attach other nodes to the tree according to the order the integers are given. When attaching a new node there is only one correct way - by adhering to three principles:

➼ always keep left subtree node values smaller than the root node value;
➼ always keep right subtree node values bigger than the root node value;
➼ both subtrees of each node are also BSTs, i.e. they recursively follow the above two principles.

Enable the computer to remember the shape of each tree diagram (recognize the images in any ways that work).

With a handful of tree diagrams in memory, you have to compare their shapes. Although the node values between the diagrams can be different, some of the diagrams could share the same shape. Find these "same looked" diagrams. Report your findings.


#### Examples

To illustrate what is "same look", some examples are given.

5 9 8 1 7        6 10 9 8 5        5 2 7 3 10        7 9 4 2 10

    5                6                 5                 7
  ╱   ╲            ╱   ╲             ╱   ╲              ╱ ╲
 1     9          5     10          2     7            4   9
       ╱                ╱           ╲      ╲          ╱     ╲
      8                9             3     10        2      10
      ╱                ╱
     7                8



The first and second tree diagrams have the same topology, the same 'look', different from the third and fourth ones. There are 4 tree diagrams but only 3 distinct shapes.
Input
Line 1: Integers n and k, space separated. n for the number of lists to compare. k for the number of nodes in each list.
Next n lines: Each line has k positive integers unique in values, space separated, for building a binary search tree. After processing n lists you will have n tree diagrams for comparing against each other.
Output
Line 1 : The number of distinct tree diagram shapes in all the given lists.
Constraints
1 ≤ n ≤ 200
1 ≤ k ≤ 16
1 ≤ node values ≤ 999
Example
Input

4 5
5 9 8 1 7
6 10 9 8 5
5 2 7 3 10
7 9 4 2 10

Output

3



### Some solutions from OTHER devs - NOT MY CODE

```python
from functools import reduce
import re

def insert(tree, value):
    if tree is None:
        return {'V': value, 'L': None, 'R': None}
    if value > tree['V']:
        tree['R'] = insert(tree['R'], value)
    else:
        tree['L'] = insert(tree['L'], value)
    return tree

n, k = map(int, input().split())
trees = [
    reduce(insert, map(int, input().split()), None)
    for i in range(n)
]
print(len({re.sub(r"\d+", "x", str(t)) for t in trees}))
```

```python
n, k = map(int, input().split())
shapes, distinct, node = [], 0, lambda x: {'v': x, 'l': None, 'r': None}
for _ in range(n):
    values = list(map(int, input().split()))
    root = node(values.pop(0))
    for v in values:
        i = root
        while i[(side := 'l' if v < i['v'] else 'r')]: i = i[side]
        i[side] = node(v)
    shapes.append(list(x for x in str(root) if x in 'lr'))
    if all(shapes[-1] != b for b in shapes[:-1]): distinct += 1
print(distinct)
```

```python
def add_to_tree(tree, value):
    if len(tree) == 0:
        tree += [value, [], []]
    elif value < tree[0]:
        add_to_tree(tree[1], value)
    else:
        add_to_tree(tree[2], value)

n, k = map(int, input().split())
unique = set()
for i in range(n):
    root, *rest = map(int, input().split())
    tree = [root,[],[]]
    for value in rest:
        add_to_tree(tree, value)
    unique.add(''.join(x for x in str(tree) if not x.isdigit()))

print(len(unique))
```