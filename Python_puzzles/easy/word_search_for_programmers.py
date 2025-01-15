import sys

class WordSearch:
    def __init__(self, n: int, grid: list, clues: list):
        self.n = n
        self.grid = grid
        print('\n'.join([''.join(row) for row in grid]), file=sys.stderr, flush=True)
        self.solution = [list(" " * n) for i in range(n)]
        self.clues = list(map(str.upper, clues))
        print(clues, file=sys.stderr, flush=True)
        self.check_rows()
        self.check_cols()
        self.check_diagonals_down()
        self.check_diagonals_up()

    def light_up(self, i: int, j: int):
        self.solution[i][j] = self.grid[i][j]

    def check_rows(self):
        n = self.n
        rows = [''.join(row) for row in self.grid]
        for i, row in enumerate(rows):
            for clue in self.clues:
                if clue in row:
                    k = row.index(clue)
                    p = k + len(clue)
                    for j in range(k, p, 1):
                        self.light_up(i, j)
                    self.clues.remove(clue)
                if clue in row[::-1]:
                    k = n - 1 - row[::-1].index(clue)
                    p = k - len(clue)
                    for j in range(k, p, -1):
                        self.light_up(i, j)
                    self.clues.remove(clue)

    def check_cols(self):
        n = self.n
        for j in range(n):
            col = ''.join([self.grid[i][j] for i in range(n)])
            for clue in self.clues:
                if clue in col:
                    k = col.index(clue)
                    p = k + len(clue)
                    for i in range(k, p, 1):
                        self.light_up(i, j)
                    self.clues.remove(clue)
                if clue in col[::-1]:
                    k = n - 1 - col[::-1].index(clue)
                    p = k - len(clue)
                    for i in range(k, p, -1):
                        self.light_up(i, j)
                    self.clues.remove(clue)
    
    def check_diagonals_down(self):
        n = self.n
        diag_down = []
        for offset in range(n):
            diag_down.append(''.join([self.grid[i][i + offset] for i in range(n - offset)]))
            if offset:
                diag_down.append(''.join([self.grid[i + offset][i] for i in range(n - offset)]))
        for d, diag in enumerate(diag_down):
            for clue in self.clues:
                if clue in diag:
                    self.mark_diag_down(clue, d, diag, reverse=False)
                elif clue in diag[::-1]:
                    self.mark_diag_down(clue, d, diag[::-1], reverse=True)

    def mark_diag_down(self, clue: str, d: int, diag:str, reverse: bool):
        idx = diag.index(clue)
        i_start = 0
        j_start = 0
        if d != 0 and d % 2 == 0:
            i_start += d // 2
        if d % 2 == 1:
            j_start += d // 2 + 1
        k0 = [idx, len(diag) - 1 - idx][reverse]
        step = [1, -1][reverse]
        for k in range(k0, k0 + step * len(clue), step):
            self.light_up(i_start + k, j_start + k)
        self.clues.remove(clue)
        return 1

    def check_diagonals_up(self):
        n = self.n
        diag_up = []
        for offset in range(n):
            diag_up.append(''.join([self.grid[n - 1 - i][i + offset] for i in range(n - offset)]))
            if offset:
                diag_up.append(''.join([self.grid[n - 1 - i - offset][i] for i in range(n - offset)]))
        for d, diag in enumerate(diag_up):
            for clue in self.clues:
                if clue in diag:
                    self.mark_diag_up(clue, d, diag, reverse=False)
                elif clue in diag[::-1]:
                    self.mark_diag_up(clue, d, diag[::-1], reverse=True)

    def mark_diag_up(self, clue: str, d: int, diag:str, reverse: bool):
        idx = diag.index(clue)
        i_start = self.n - 1
        j_start = 0
        if d != 0 and d % 2 == 0:
            i_start -= d // 2
        if d % 2 == 1:
            j_start += d // 2 + 1
        k0 = [idx, len(diag) - 1 - idx][reverse]
        step = [1, -1][reverse]
        for k in range(k0, k0 + step * len(clue), step):
            self.light_up(i_start - k, j_start + k)
        self.clues.remove(clue)
        return 1

    def __repr__(self):
        solution = '\n'.join([''.join(row) for row in self.solution])
        return f'{solution}'

def main():
    size = int(input())
    print(size, file=sys.stderr, flush=True)
    grid = []
    for i in range(size):
        grid.append(list(input()))
    clues = input().split()
    search_words = WordSearch(size, grid, clues)
    print(search_words)


if __name__ == '__main__':
    sys.exit(main())
