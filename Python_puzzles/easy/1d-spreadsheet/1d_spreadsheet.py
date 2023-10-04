import sys
import math

class Cell:
    def __init__(self, index, operation, arg_1, arg_2):
        self.index = index
        self.operation = operation
        self.arg1 = arg_1
        self.arg2 = arg_2
        if operation == 'VALUE':
            self.arg2 = "0"
        self.res = None
        self.dep1 = (arg_1[0] == '$')
        self.dep2 = (arg_2[0] == '$')
        self.get_result() 

    def get_result(self):
        opt = {'VALUE': lambda x, y: x, 'ADD': lambda x, y: x + y,
               'SUB': lambda x, y: x - y, 'MULT': lambda x, y: x * y}
        if self.dep1 or self.dep2:
            return
        self.res = opt[self.operation](int(self.arg1), int(self.arg2))

    def put_stderr(self):
        print(self.index, self.operation, self.arg1, self.arg2, self.res, self.dep1, self.dep2, file=sys.stderr, flush=True)


class SpreadSheet:
    def __init__(self, n):
        self.n = n
        self.cells = []
        self.nb_cells = 0

    def append_cell(self, operation, arg_1, arg_2):
        index = self.nb_cells
        cell = Cell(index, operation, arg_1, arg_2)
        self.cells.append(cell)
        self.nb_cells += 1

    def calculate_cell(self, index):
        cell = self.cells[index]
        if cell.dep1:
            i1 = str(cell.arg1[1:])
            idx1 = int(i1)
            if self.cells[idx1].res == None:
                self.calculate_cell(idx1)
            else:
                self.cells[index].arg1 = self.cells[idx1].res
                self.cells[index].dep1 = False
        if cell.dep2:
            idx2 = int(cell.arg2[1:])
            if self.cells[idx2].res == None:
                self.calculate_cell(idx2)
            else:
                self.cells[index].arg2 = self.cells[idx2].res
                self.cells[index].dep2 = False
        # self.cells[index].put_stderr()
        self.cells[index].get_result()

    def count_nans(self):
        count = 0
        for cell in self.cells:
            count += (cell.res == None)
        return count

    def calculate_sheet(self):
        opt = ['VALUE', 'ADD', 'SUB', 'MULT']
        while self.count_nans() > 0:
            for cell in self.cells:
                if cell.res == None and cell.operation in opt:
                    self.calculate_cell(cell.index)

    def print_to_stderr(self):
        for cell in self.cells:
            print(cell.index, cell.operation, cell.arg1, cell.arg2, cell.res, file=sys.stderr, flush=True)
    
    def print_results(self):
        for cell in self.cells:
            print(cell.res)


def main():
    n = int(input())
    sheet = SpreadSheet(n)
    print("n=", n, file=sys.stderr, flush=True)
    for i in range(n):
        operation, arg_1, arg_2 = input().split()
        sheet.append_cell(operation, arg_1, arg_2)
    # sheet.print_to_stderr()
    sheet.calculate_sheet()
    sheet.print_results()


if __name__ == '__main__':
    main()
