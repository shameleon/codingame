import sys
from the_resistance import Resistance, MorseTranslator


class TheResistanceTests:

    def test_01():
        l = '-.-'
        words = ['A', 'B', 'C', 'HELLO', 'K', 'WORLD']
        return l, words
        
    def test_02():
        l = '--.-------..'
        words = ['GOD', 'GOOD', 'MORNING', 'G', 'HELLO']
        return l, words
    
    def test_03():
        l = '......-...-..---.-----.-..-..-..'
        words = ['HELL', 'HELLO', 'OWORLD', 'WORLD', 'TEST']
        return l, words
    
    def test_05():
        l = '-.-..---.-..---.-..--'
        words = 'CAT KIM TEXT TREM CEM'.split()
        return l, words

class MorseWord:
    def __init__(self, word, word_in_morse, seq):
        self.word = word
        self.mord = word_in_morse
        self.indices = self.indices_in_seq(seq)

    def indices_in_seq(self, seq) -> list:
        if self.mord == seq:
            return [0]
        indices = []
        i = 0
        while i < len(seq) - len(self.mord):
            j = seq.find(self.mord, i, len(seq))
            if j == -1:
                break
            indices.append(j)
            i = j + 1
        return indices
    
    def is_at_index(self, start_index):
        if start_index in self.indices:
            return start_index + len(self.mord)
        return -1

    def __repr__(self):
        res = f'{self.word} {self.mord}'
        if len(self.indices) > 0:
            res += f'{self.indices}\n'
        return res

def get_mords_(morse_words, l, i):
    p = dict(zip(range(len(l)), [] * len(l))) 
    for mord in morse_words:
        j = mord.is_at_index(i)
        if j > -1:
            

def main():
    """ 
    l: Morse sequence length
    n: the number of words in the dictionnary
    w: following lines: one word from the dictionary per line.
    Each word has a maximum length M 
    and only appears once in the dictionary.
    """
    tests = [TheResistanceTests.test_01,
             TheResistanceTests.test_02,
             TheResistanceTests.test_03,
             TheResistanceTests.test_05
             ]
    translate = MorseTranslator()
    for test_input in tests:
        l, words = test_input()
        print(l, file=sys.stderr, flush=True)
        print(words, file=sys.stderr, flush=True)
        morse_words = []
        for word in words:
            m = translate.morsed(word)
            if m in l:
                morse_words.append(MorseWord(word, m, l))
        get_combination(l, morse_words, 0)

        print(morse_words)

if __name__ == "__main__":
    main()