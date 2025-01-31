import sys
import re

""" progress 50% - KO test04. 5, 7:10 validators failed"""

class MorseTranslator:
    def __init__(self):
        self.morse_code = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.',
                               H='....', I='..', J='.---', K='-.-', L='.-..', M='--', N='-.',
                               O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-',
                               V='...-', W='.--', X='-..-', Y='-.--', Z='--..')

    def to_morse(self, word):
        return ''.join(self.morse_code[c] for c in word)


class MorseWord:
    def __init__(self, word, word_in_morse, seq):
        self.word = word
        self.mord = word_in_morse
        self.indices = self.indices_in_seq(seq)

    def indices_in_seq(self, seq) -> list:
        return [match.start() for match in re.finditer(f'(?={self.mord})', seq)]
    
    def from_index_to_next_index(self, start_index):
        if start_index in self.indices:
            return start_index + len(self.mord)
        return -1

    def __repr__(self):
        res = f'{self.word} {self.mord}'
        if len(self.indices) > 0:
            res += f'{self.indices}\n'
        return res


class Resistance:
    def __init__(self, sequence: str):
        """ """
        self.seq = sequence
        self.mord_set = set()
        self.alpha = MorseTranslator()
        self.mem = dict()

    def add_new_input_word(self, word: str):
        mord = self.alpha.to_morse(word)
        if mord in self.seq:
            self.mord_set.add(MorseWord(word, mord, self.seq))

    def get_mords_at_index(self, i):
        if i == len(self.seq):
            return 1
        if i in self.mem:  # Vérifie si on a déjà calculé cet index
            return self.mem[i]
        total_at_index = 0
        for mord in self.mord_set:
            j = mord.from_index_to_next_index(i)
            if j > -1:
                total_at_index += self.get_mords_at_index(j)
        self.mem[i] = total_at_index
        return total_at_index

    def number_of_solutions(self):
        print(len(self.mord_set), "mords", file=sys.stderr, flush=True)
        return self.get_mords_at_index(0)


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
    resist = Resistance(l)
    for _ in range(n):
        resist.add_new_input_word(input())
    result = resist.number_of_solutions()
    print(result)


if __name__ == "__main__":
    sys.exit(main())
