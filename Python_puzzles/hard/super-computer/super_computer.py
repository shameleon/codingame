import sys
import math

"""
    objective : obtain the maximum jobs to do 
                based on a set of dates
"""


class ComputerPlanner:
    def __init__(self, n):
        self.reserved = []
        self.booked = []

    def _remove_overlapping_dates(self):
        """ check date overlap with last booked slot """
        for idx, date in enumerate(self.reserved):
            if idx == 0:
                self.booked.append(date)
            else:
                prev = self.booked[-1]
                if idx == 0 or date[0] > prev[1]:
                    self.booked.append(date)

    def find_best_dates(self):
        """
        1/ sort by ending day
        2/ compare each element with the last booked slot
        3/ book the slot if there is no days overlap 
        """
        self.reserved.sort(key=lambda x : x[1])
        print("len =", len(self.reserved),
              "max_value =", self.reserved[-1][1],
              file=sys.stderr, flush=True)
        self._remove_overlapping_dates()
        return len(self.booked)

    def push(self, j, d):
        """ push list [date of begin, date of end] to list """
        begin = j
        end = j + d - 1
        self.reserved.append([begin, end])

    def print_reservations(self):
        for date in self.reserved:
            print(f'{date}', end=' < ', file=sys.stderr, flush=True)
        print("end\n.")


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


