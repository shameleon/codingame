import sys


class Rectangle:
    def __init__(self, h, w, y0, x0):
        self.h, self.w = h, w
        self.rect = {'ys': [0, h], 'xs': [0, w]}
        self.moves = []
        self.moves.append([y0, x0])

    def update_bomb_dir(self, bomb_dir):
        yi, xi = self.moves[-1]
        self.define_boundaries(bomb_dir, yi, xi)
        return " ".join(str(x) for x in self.get_next_move()[::-1])

    def define_boundaries(self, bomb_dir, y, x):
        if 'U' in bomb_dir:
            self.rect['ys'][1] = y - 1
        elif 'D' in bomb_dir:
            self.rect['ys'][0] = y + 1
        if 'R' in bomb_dir:
            self.rect['xs'][0] = x + 1
        elif 'L' in bomb_dir:
            self.rect['xs'][1] = x - 1

    def get_next_move(self):
        ys = self.rect['ys']
        xs = self.rect['xs']
        y = (ys[0] + ys[1]) // 2
        x = (xs[0] + xs[1]) // 2
        self.moves.append([y, x])
        return [y, x]


def main():
    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]
    print(w, h, n, file=sys.stderr, flush=True)
    print(x0, y0, file=sys.stderr, flush=True)
    grid = Rectangle(h, w, y0, x0)
    # game loop
    while True:
        # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        # Print the location of the next window Batman should jump to.
        print(grid.update_bomb_dir(input()))


if __name__ == '__main__':
    sys.exit(main())
 
