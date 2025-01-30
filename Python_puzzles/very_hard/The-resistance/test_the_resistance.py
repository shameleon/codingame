import sys
from the_resistance import Resistance, MorseWord, MorseTranslator


class TheResistanceTests:
    def test_01():
        l = '-.-'
        words = ['A', 'B', 'C', 'HELLO', 'K', 'WORLD']
        return l, words, 1
        
    def test_02():
        l = '--.-------..'
        words = ['GOD', 'GOOD', 'MORNING', 'G', 'HELLO']
        return l, words, 1
    
    def test_03():
        l = '......-...-..---.-----.-..-..-..'
        words = ['HELL', 'HELLO', 'OWORLD', 'WORLD', 'TEST']
        return l, words, 2
    
    def test_05():
        l = '-.-..---.-..---.-..--'
        words = 'CAT KIM TEXT TREM CEM'.split()
        return l, words, 125


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
    outcomes = []
    for test_input in tests:
        l, words, answer= test_input()
        print(l, file=sys.stderr, flush=True)
        print(words, file=sys.stderr, flush=True)
        resist = Resistance(l)
        for word in words:
            resist.add_new_input_word(word)
        result = resist.number_of_solutions()
        print(result)
        outcomes.append(['KO', 'OK'][result == answer])
    print(dict(zip(range(len(tests)), outcomes)), file=sys.stderr, flush=True)


if __name__ == "__main__":
    sys.exit(main())