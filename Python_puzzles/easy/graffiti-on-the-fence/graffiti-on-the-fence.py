import sys
import math

"""
    st      ed
    !░░░░░░░░!
          !░░░░░░░░!
                         !░░░░░░░░!
 +--+--+--+--+--+--+--+--+--+--+--+--+
 0  1  2  3  4  5  6  7  8  9  10 11 12

 ouput :
 0 1
 6 8
 11 12
"""


class Section():
    def __init__(self, st, ed, painted = True):
        self.st = st
        self.ed = ed
        self.painted = painted

    def start(self) -> int:
        return self.st
    
    def end(self) -> int:
        return self.ed


class Fence():
    def __init__(self, l, n):
        self.l = l
        self.n = n
        self.paintings = []
        self.unpainted = []
    
    def add_paint(self, st, ed):
        painting = Section(st, ed)
        self.paintings.append(painting)
    
    def _sort_sections(self, sections: list):
        """In-place sorting of a list of Sections objects by start attribute"""
        sections.sort(key=lambda x: x.start())

    def _print_sections_to_std_err(self, sections: list):
        [print(f"{section.st} {section.ed}", file=sys.stderr, flush=True) for section in sections]

    def _print_sections(self, sections: list):
        print("_" * 20, file=sys.stderr, flush=True)
        if len(sections) == 0:
            print("All painted", end='')
        else:
            [print(f"{section.st} {section.ed}") for section in sections[:-1]]
            print(f"{sections[-1].st} {sections[-1].ed}", end='') 

    def _find_next_unpainted(self, it, idx) -> None:
        if idx >= len(self.paintings):
            if it < self.l:
                self.unpainted.append(Section(it, self.l, False))
            return
        start = it
        end = self.paintings[idx].start()
        print(f"next {it} {idx} {start} {end}", file=sys.stderr, flush=True) 
        if start < end:
            self.unpainted.append(Section(start, end, False))
        it = max(it, self.paintings[idx].end())
        self._find_next_unpainted(it, idx + 1)

    def output_unpainted(self):
        """sort painting by start"""
        self._sort_sections(self.paintings)
        self._print_sections_to_std_err(self.paintings)
        self._find_next_unpainted(0, 0)
        self._print_sections(self.unpainted)
        print ()


def main():
    """
    Input:
    An integer l for the total length of the fence in meter
    An integer n for the number of reports.
    A painted section is reported as st ed
    which means painting is done from [starting point] to [ending point]. 
    
    Output :
    A list of unpainted sections, one section on each line, by format st ed,
    sorted by st in ascending order.
    """
    l = int(input())
    n = int(input())
    fence = Fence(l, n)
    print(f"l = {l}   n = {n}", file=sys.stderr, flush=True)
    for i in range(n):
        st, ed = [int(j) for j in input().split()]
        fence.add_paint(st, ed)
        # print(f"{st}-{ed}", file=sys.stderr, flush=True)
    fence.output_unpainted()


if __name__ == "__main__":
    main()

