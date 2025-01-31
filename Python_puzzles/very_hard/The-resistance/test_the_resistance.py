import sys
import time

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

    def test_04():
        """len(l) = 9884 and n = 9444, only 2109 words are matching"""
        l = '. ... - / --.- ..- .. -.. . -- / - . -- .--. --- .-. .- / .- ..- - / .--. .-.. .- -.-. . .- - / -.. --- .-.. --- .-. . / . ..- -- / --- -- -. .. ... / --.-..-.....'.replace('/', '').replace(' ', '')
        words = 'Lorem ipsum dolor sit amet Quo ratione molestiae est quidem tempora aut placeat dolore Eum omnis Quis vel odio facere qui modi reiciendis est ducimus consequuntur ea molestiae consequuntur At explicabo quia Ut fugit voluptatem aut velit provident ut quis illo sed delectus voluptatibus vel praesentium dolore Sit nostrum suscipit non numquam nisi quo maxime eligendi rem voluptas quia est consequatur cupiditate et deleniti reiciendis'.upper().split()
        return l, words, 37058040666

    def test_05():
        l = '-.-..---.-..---.-..--'
        words = 'CAT KIM TEXT TREM CEM'.split()
        return l, words, 125

    def test_06():
        l = '..............................................'
        words = ['E', 'I']
        return l, words, 2971215073

    def test_07():
        """ LOREM IPSUM"""
        l = '.-..---.-..--...--......---.-..---.-..--...--......---.-..---.-..--...--......---.-..---.-..--...--......---.-..---.-..--...--......---'
        words = ['LOREM', 'IPSUM', 'LOREM']
        return l, words, 32


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
             TheResistanceTests.test_05,
             TheResistanceTests.test_04,
             TheResistanceTests.test_06,
             TheResistanceTests.test_07
             ]
    outcomes = []
    for test_input in tests:
        start = time.time()
        l, words, answer= test_input()
        print(l, file=sys.stderr, flush=True)
        print("len(l) =", len(l), file=sys.stderr, flush=True)
        print(words, file=sys.stderr, flush=True)
        resist = Resistance(l)
        for word in words:
            resist.add_new_input_word(word)
        result = resist.number_of_solutions()
        end = time.time()
        print(result)
        print("Wall time =", end - start)
        outcomes.append(['KO', 'OK'][result == answer])
    print(dict(zip(range(len(tests)), outcomes)), file=sys.stderr, flush=True)


if __name__ == "__main__":
    sys.exit(main())