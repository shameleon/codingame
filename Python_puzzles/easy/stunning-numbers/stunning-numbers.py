import sys

"""
    80% success - 2 validators not ok
"""

class  StunningNumberSearch:
    def __init__(self, nb:str):
        self.nb = nb
        print(["false", "true"][check_if_stunning(nb)])
        self.next_sn = self.get_next_stunnning_number(nb)
        print(self.next_sn)

    def get_next_stunnning_number(self, nb: str):
        flippable_digit    = '012--56-89'
        next_flippable     = '0125556889'   
        symetric           = '012--59-86'
        l = len(nb)
        has_mid = (l % 2 == 1)
        size = l // 2 + 1 * has_mid
        left = str(int((nb[:size])) + 1)
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
        if check_if_stunning(res):
            return res
        return self.stun_the_middle(res)
    
    def stun_the_middle(self, nb: str):
        next_self_symetric = '1888888800'
        next_flippable     = '1255568890'   
        symetric           = '012--59-86'
        l = len(nb)
        if not l % 2:
            return nb
        mid = l // 2
        c = next_self_symetric[int(nb[mid])]
        nb = replace(nb, mid, c)
        if c == '0':
            if l == 1:
                return '11'
            left_c = next_flippable[int(nb[mid - 1])]
            nb = replace(nb, mid - 1, left_c)
            right_c = symetric[int(left_c)]
            nb = replace(nb, mid + 1, right_c)
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
    if len(nb) % 2 and nb[len(nb) // 2] not in '018':
            return False
    if nb == flip_number(nb):
        return True
    return False


def main():
    """ tests """
    numbers = ['3', '69', '161', '9987', '654321', '1260921',
               '88888888', '123456789', '314159265359',
               '6920158510269']
    answers = ['8', '88', '181', '10001', '655559', '1261921',
               '88896888', '125000521', '500000000005',
               '6920160910269']
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
    print(f'{result.count('OK')} / {len(answers)}')

if __name__ == "__main__":
    sys.exit(main())

