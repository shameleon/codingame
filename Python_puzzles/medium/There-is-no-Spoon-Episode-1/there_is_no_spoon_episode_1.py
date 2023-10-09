import sys
import math

""" progress 100% """

class Node:
    def __init__(self, y, x, right=None, bottom=None):
        """ node for a linked-list connected
        to right an to bottom"""
        self.y = y
        self.x = x
        self.right = right
        self.bottom = bottom
        self.visited = False

    def set_bottom(self, bottom):
        self.bottom = bottom

    def get_xy(self):
        return f'{self.x} {self.y}'

    def cell_output(self):
        """ Three coordinates: a node,
                               its right neighbor,
                               its bottom neighbor.
        if either right or bottom nodes 
        are not found, -1 -1 is representing
        the missing x y pair """ 
        if self.right is None:
            right = '-1 -1'
        else:
            right = self.right.get_xy()
        if self.bottom is None:
            bottom = '-1 -1'
        else:
            bottom = self.bottom.get_xy()
        return (f'{self.get_xy()} {right} {bottom}')


class NoSpoon:
    def __init__(self, arr, w, h):
        """ A network of cells is created from an array"""
        self.w = w
        self.h = h
        self.arr = arr
        self.cells = []
        self.create_cells()

    def create_cells(self,):
        """ constructs all the needed nodes 
        from right to left, connecting them by the right""" 
        for y in range(self.h):
            right = None
            for x in range(self.w)[::-1]:
                if self.arr[y][x] == '0':
                    new = Node(y, x)
                    self.cells.append(Node(y, x, right=right))
                    right = new
        self.connect_bottoms()

    def connect_bottoms(self):
        for x in range(self.w):
            bottom = None
            for y in range(self.h)[::-1]:
                if self.arr[y][x] == '0':
                    cell = self.find_cell(y, x)
                    if cell != None:
                        if bottom != None:
                            cell.set_bottom(bottom)
                        bottom = cell

    def find_cell(self, y, x):
        """ print cells to stdout""" 
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def cells_to_print(self):
        """ print cells to stdout""" 
        for cell in self.cells:
            print(cell.cell_output())


if __name__ == "__main__":
    width = int(input())
    height = int(input())
    arr = [input() for i in range(height)]
    there_is = NoSpoon(arr, width, height)
    there_is.cells_to_print()
