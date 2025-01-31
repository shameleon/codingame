import sys

""" Success 100%"""


class MorseTranslator:
    def __init__(self):
        self.morse_code = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.',
                               H='....', I='..', J='.---', K='-.-', L='.-..', M='--', N='-.',
                               O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-',
                               V='...-', W='.--', X='-..-', Y='-.--', Z='--..')

    def to_morse(self, word):
        return ''.join(self.morse_code[c] for c in word)


class Resistance:
    def __init__(self, sequence: str):
        self.seq = sequence
        self.mords = []
        self.alpha = MorseTranslator()
        self.mem = dict()

    def add_new_input_word(self, word: str):
        mord = self.alpha.to_morse(word)
        if self.seq.find(mord) > -1:
            self.mords.append(mord)

    def get_mords_at_index(self, i):
        if i == len(self.seq):
            return 1
        if i in self.mem:
            return self.mem[i]
        total_at_index = 0
        for mord in self.mords:
            j = i + len(mord)
            if mord == self.seq[i:j]:
                total_at_index += self.get_mords_at_index(j)
        self.mem[i] = total_at_index
        return total_at_index

    def number_of_solutions(self):
        print("nb of matching words =", len(self.mords), file=sys.stderr, flush=True)
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
    print("sequence length =",len(l), file=sys.stderr, flush=True)
    print("nb of words =", n, file=sys.stderr, flush=True)
    resist = Resistance(l)
    for _ in range(n):
        resist.add_new_input_word(input())
    result = resist.number_of_solutions()
    print(result)


if __name__ == "__main__":
    sys.exit(main())
