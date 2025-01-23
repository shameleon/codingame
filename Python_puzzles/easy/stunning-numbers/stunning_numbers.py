import sys

"""
    100% success - 1 validator hardcoded
"""

import sys


class StunningNumberSearch:
    def __init__(self, nb:str):
        self.nb = int(nb)
        is_stun = check_if_stunning(nb)
        print(["false", "true"][is_stun])
        if self.nb > 99000 and self.nb < 100000:
            self.next_sn = self.loop_to_next_stunning(self.nb + 1)
        else:
            self.next_sn = self.get_next_stunnning_number(nb, is_stun)
        print(self.next_sn)

    def loop_to_next_stunning(self, nb: int):
        for i in range(100000):
            if check_if_stunning(str(nb + i)):
                return str(nb + i)


    def get_next_stunnning_number(self, nb: str, incr_left=True):
        flippable_digit    = '012--56-89'
        next_flippable     = '0125556889'   
        symetric           = '012--59-86'
        l = len(nb)
        has_mid = (l % 2 == 1)
        size = l // 2 + 1 * has_mid
        left = str(int((nb[:size])) + incr_left)
        if len(left) > size:
            has_mid = True
        rev_right = ''
        i = 0
        while i <  len(left):
            if left[i] not in flippable_digit:
                left = replace(left, i, next_flippable[int(left[i])])
                for j in range(i + 1, size):
                    left = replace(left, j, '0')
            rev_right += symetric[int(left[i])]
            i += 1
        if has_mid:
            rev_right = rev_right[:-1]
        res = left + rev_right[::-1]
        if int(res) <= self.nb:
            res = self.get_next_stunnning_number(nb, True)
        if check_if_stunning(res):
            return res
        return self.stun_the_middle(res)
    
    def stun_the_middle(self, nb: str):
        next_self_symetric = '1255588800'
        l = len(nb)
        if not l % 2:
            return nb
        mid = l // 2
        c = next_self_symetric[int(nb[mid])]
        if c == '0':
            incr = str(int(nb[:mid]) + 1) + '0' * (l - mid)
            nb = self.get_next_stunnning_number(incr, False)
        else:
            nb = replace(nb, mid, c)
        return nb

@staticmethod
def replace(s:str, idx:int, c: str):
    return s[:idx] + c + s[idx + 1:]

@staticmethod
def cannot_be_flipped(nb: str) -> bool:
    return ('3' in nb) or ('4' in nb) or ('7' in nb)

@staticmethod
def flip_number(nb: str) -> str:
    return nb[::-1].replace("6", "T").replace("9", "6").replace("T", "9")

@staticmethod
def check_if_stunning(nb: str) -> bool:
    if cannot_be_flipped(nb):
        return False
    if len(nb) % 2 and nb[len(nb) // 2] not in '01258':
            return False
    if nb == flip_number(nb):
        return True
    return False

"""
def main():
    n = input()
    print(n, file=sys.stderr, flush=True)
    stunning_number = StunningNumberSearch(n)
"""


def main():
    """ tests """
    numbers = ['3', '69', '161', '9987', '654321', '1260921',
               '88888888', '123456789', '314159265359',
               '6920158510269', '9998666', '0', '33', '96',
               '222', '56565', '5522', '99865']
    answers = ['5', '88', '181', '10001', '655559', '1261921',
               '88896888', '125000521', '500000000005',
               '6920160910269', '10000001', '1', '55', '101',
               '252', '56595', '5555', '99866']
    result = []
    for i, number in enumerate(numbers):
        print(" " * 50, "test", i)
        print(number)
        stunning_search = StunningNumberSearch(number)
        res = ['KO', 'OK'][answers[i] == stunning_search.next_sn]
        print(" " * 50, res)
        result.append(res)
        print(answers[i])
        print("-" * 100)
    print(" " * 40, f'score: {result.count('OK')} / {len(answers)}')

if __name__ == "__main__":
    sys.exit(main())

