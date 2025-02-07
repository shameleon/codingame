# Vox Codei - episode 2

[Codingame : Vox Codei - episode 2](https://www.codingame.com/training/expert/vox-codei-episode-2)

`Pattern recognition` `DFS` `Brute-force`


### Best score

20

### The Goal

You access the central computer's firewall interface via Viktor's tablet. The firewall is comprised of surveillance nodes.

This puzzle is the second level of Vox Codei: your objective is still to destroy these nodes by overloading them with the help of fork-bombs, but this time the nodes are moving!

Note: the input is slightly different from the previous puzzle, but you can reuse part of your solution.
  Rules
The interface is presented by a rectangular grid, of variable width and height. It is provided at the beginning of each game in the shape of a table of characters.

Details:
 

    Several surveillance nodes (@) are positioned on the grid.

    Indestructible and passive nodes (#) can also be present on the grid.

    You have a fixed number of bombs to use at the start of the game.

    Each game turn, you may either place a bomb on the grid or wait.

    The fork-bombs explode 3 turns after having been placed.

    Bombs explode in a cross shape. They have a range of 3 cells (see schema further down).

    The bombs will destroy every node the explosion comes into contact with. Explosions do not go through passive nodes.

    A fork-bomb can explode before the 3 turns if it is triggered by the explosion of another fork-bomb.

    You cannot place a bomb on a node. You must place them on empty cells (.) of the grid.

    You have a limited amount of turns in which to destroy all of the surveillance nodes, or you will be detected and lose the game.

    Some surveillance nodes (@) moves on the grid. Their movement is only vertical or horizontal. Their speed is constant and is equal to one unit per turn.

    If a moving node touches a passive node (#) or the grid limit, it changes its direction..

 
Victory Conditions
You will win once all of the surveillance nodes have been destroyed in the allotted amount of turns
  Example

...@...
...#...
.......
.....@@
.......
.......
.......

Example for the explosion of a bomb placed at (3, 3) in the following interface grid.

The two nodes to the right are destroyed by the blast. The top node is protected by the indestructible passive node.
1rst round
The fork-bomb has been placed
2nd round
The fork-bomb is charging
3rd round
The bomb explodes
  Note
Don’t forget to run the tests by launching them from the “Test cases” window.

The tests provided are similar to the validation tests used to compute the final score but are slightly different.
  Game Input
The program must first read the initialization data from standard input. Then, within an infinite loop, read the contextual data (number of bombs and remaining turns) from the standard input and provide the next instruction to standard output. The protocol is detailed further down.
Initialization input

Line 1: 2 integers width and height. They correspond to the size of the grid.
Input for one game turn

Line 1: 2 integers rounds and bombs. They correspond to the number of turns remaining before detection and the number of bombs still available to you.

height next lines: 1 string mapRow of length width. Each line corresponds to a row in the grid. The . represents an empty cell, @ represents surveillance node and # represents a passive node.
Output for one game turn
A single line (including newline character) to indicate which action to take:

    Either the keyword WAIT to do nothing
    or the (x, y) coordinates in the grid of where you want to place a fork-bomb (2 integers separated by a space). The (0,0) coordinate is located in the upper-left corner of the grid

Constraints
2 < width, height < 20
3 < rounds < 20
0 < bombs < 10
0 <= x < width
0 <= y < height
Duration of one game turn: 100 ms
