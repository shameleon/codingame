import sys
from super_computer import CalcPlanner

def test_super_computer_planner(n, input):
    cal = CalcPlanner(n)
    for date in input:
        print(input, end=',', file=sys.stderr, flush=True)
        cal.push(date[0], date[1])
    return cal.find_dates()

def test3():
    """ """
    n = 16
    input = [[6, 3], [12, 8], [9, 2], [12, 2],
             [22, 5], [27, 2], [21, 3], [25, 2], 
             [32, 4], [15, 3], [19, 2], [4, 1],
             [5, 6], [14, 15], [30, 2], [34, 8]]
    res = test_super_computer_planner(n, input)
    ans = 11
    print("test3", (res == ans) * "[OK]" + (res != ans) * "** FAIL **" )


def test2():
    """ one overlap
    
    6-8 _____ 12-19 ______ 22-26 ... 27-29 ... 32-35 
         |_ 15-17_19-21_|
    """
    n = 7
    input = [[6, 3], [12, 8], [22, 5], [27, 2],
             [32, 4], [15, 3], [19, 3]]
    res = test_super_computer_planner(n, input)
    ans = 6
    print("test2", (res == ans) * "[OK]" + (res != ans) * "** FAIL **" )


def test1():
    """linear, no overlap"""
    n = 5
    input = [[6, 3], [12, 8], [22, 5], [27, 2], [32, 4]]
    res = test_super_computer_planner(n, input)
    print("test1", (res == 5) * "[OK]" + (res != 5) * "** FAIL **" )


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    test1()