import sys
import math

"""
80% success, fails on big numbers
"""
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
class  StunningNumber:
    def __init__(self, n):
        self.n = n
        print(["false", "true"][check_if_stunning(str(n))])
        self.loop_to_next_stunnning_number()

    def loop_to_next_stunnning_number(self):
        n = self.n
        while True:
            n += 1
            if check_if_stunning(str(n)):
                print(n)
                break

@staticmethod
def cannot_be_flipped(nb : str) -> bool:
    return ('3' in nb) or ('4' in nb) or ('7' in nb)

@staticmethod
def flip_number(nb : str) -> str:
    return nb[::-1].replace("6", "T").replace("9", "6").replace("T", "9")

@staticmethod
def check_if_stunning(nb : str) -> bool:
    if cannot_be_flipped(nb):
        return False
    if nb == flip_number(nb):
        return True
    return False

def main():
    n = int(input())
    print("input :", n, file=sys.stderr, flush=True)
    stunning_number = StunningNumber(n)

if __name__ == "__main__":
    sys.exit(main())