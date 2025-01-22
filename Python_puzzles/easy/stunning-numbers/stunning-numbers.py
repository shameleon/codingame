import sys

"""

"""

class  StunningNumberSearch:
    def __init__(self, nb:str):
        self.nb = nb
        print(["false", "true"][check_if_stunning(nb)])
        self.next_sn = self.get_next_stunnning_number(nb))
        print(self.next_sn)

    def get_next_stunnning_number(self, nb: str):
        """" 99 87 100"""
        flippable_digit = '012--56-89'
        next_flippable = '0125556889'   
        symetric = '012--59-86'
        next_self_symetric = '018888888*'
        l = len(nb)
        left = ['', nb[:l // 2]][l >= 2]
        mid = ['', nb[l//2]][l % 2 == 1]
        rev_right = ''
        print(left, mid, '-' * (l // 2))
        if len(mid):
            mid = next_self_symetric[int(mid)]
        if len(left):
            for i , c in enumerate(left):
                if c not in flippable_digit:
                    left = replace(left, i, next_flippable[int(c)])
                rev_right += symetric[int(left[i])]

        res = left + mid + rev_right[::-1]
        #if check_if_stunning(res):
        return res
        print("res", res, "stun?", check_if_stunning(res))

""" incr mid if any"""

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
    if nb == flip_number(nb):
        return True
    return False


def main():
    # KO '9987', '10001', 99, 101
    numbers = ['69', '161', '9987', '654321', '1260921',
               '88888888', '123456789', '6920158510269']
    answers = ['88', '181', '10001', '655559', '1261921',
               '88896888', '125000521', '6920160910269']
    result = []
    for i, number in enumerate(numbers):
        print(number)
        stunning_search = StunningNumberSearch(number)
        res = ['KO', 'OK'][answers[i] == stunning_search.next_sn]
        print(" " * 50, res)
        result.append(res)
        print(answers[i])
        print("-" * 100)
    print(f'{result.count('OK')} / {len(answers)}')

if __name__ == "__main__":
    sys.exit(main())

