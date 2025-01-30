import sys
import math
from itertools import permutations 

""" progreess 10%"""
class MorseTranslator:
    def __init__(self):
        self.morse_code = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.',
                          H='....', I='..', J='.---', K='-.-', L='.-..', M='--', N='-.',
                          O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-',
                          V='...-', W='.--', X='-..-', Y='-.--', Z='--..')
    def morsed(self, word):
        mord = ""
        for s in word:
            mord += self.morse_code[s]
        return mord


class Resistance:
    def __init__(self, sequence, words):
        """ """
        self.translate = MorseTranslator()
        self.seq = sequence
        mords = [self.translate.morsed(word) for word in words]
        matches = {idx: mord in sequence for idx, mord in enumerate(mords)}
        self.matches = {k: v for k, v in matches.items() if v}
        self.idx = set(self.matches.keys())
        print(self.idx, file=sys.stderr, flush=True)

    def _permutate(self):
        permut_set = permutations(self.idx)
        count = len(self.idx)
        for perm in permut_set:
            pass

        # dict for ans
        pass

def main():
    """ 
    l: Morse sequence length
    n: the number of words in the dictionnary
    w: following lines: one word from the dictionary per line.
    Each word has a maximum length M 
    and only appears once in the dictionary.
    """
    l = input()
    n = int(input())
    print(l, file=sys.stderr, flush=True)
    print(n, file=sys.stderr, flush=True)
    words = [input() for i in range(n)]
    decode = Resistance(l, n, words)
    [print(word, file=sys.stderr, flush=True) for word in words]
    print("2")

if __name__ == "__main__":
    main()
