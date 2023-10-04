import sys
import math

"""
    objective : obtain the maximum jobs to do 
                based on a set of dates
"""

class ComputerPlanner:
    def __init__(self, n):
        self.reservations = []

    def _remove_overlapping_dates(self):
        """ remove current date if it overlap with previous """
        for idx, date in enumerate(self.reservations):
            if idx != 0:
                if date[0] <= self.reservations[idx - 1][1]:
                    self.reservations.pop(idx)

    def find_best_dates(self):
        """
        1/ sort by date of end 
        2/ pop element if its date overlap with previous element
        """
        self.reservations.sort(key=lambda x : x[1])
        print("len =", len(self.reservations),
              "max_value =", self.reservations[-1][1],
              file=sys.stderr, flush=True)
        self._remove_overlapping_dates()
        return len(self.reservations)

    def push(self, j, d):
        """ push list [date of begin, date of end] to list """
        begin = j
        end = j + d - 1
        self.reservations.append([begin, end])


def main():
    n = int(input())
    cal = ComputerPlanner(n)
    for i in range(n):
        j, d = [int(j) for j in input().split()]
        cal.push(j, d)
    max_jobs = cal.find_best_dates()
    print(max_jobs)


if __name__ == "__main__":
    main()


