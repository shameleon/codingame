import sys


class NatoAlphabets:
    def __init__(self):
        year_1908 = "Authority, Bills, Capture, Destroy, Englishmen, Fractious, Galloping, High, Invariably, Juggling, Knights, Loose, Managing, Never, Owners, Play, Queen, Remarks, Support, The, Unless, Vindictive, When, Xpeditiously, Your, Zigzag"
        year_1917 = "Apples, Butter, Charlie, Duff, Edward, Freddy, George, Harry, Ink, Johnnie, King, London, Monkey, Nuts, Orange, Pudding, Queenie, Robert, Sugar, Tommy, Uncle, Vinegar, Willie, Xerxes, Yellow, Zebra"
        year_1927 = "Amsterdam, Baltimore, Casablanca, Denmark, Edison, Florida, Gallipoli, Havana, Italia, Jerusalem, Kilogramme, Liverpool, Madagascar, New-York, Oslo, Paris, Quebec, Roma, Santiago, Tripoli, Uppsala, Valencia, Washington, Xanthippe, Yokohama, Zurich"
        year_1956 = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu"
        self.alphabets = []
        self.alphabets.append(year_1908.split(", "))
        self.alphabets.append(year_1917.split(", "))
        self.alphabets.append(year_1927.split(", "))
        self.alphabets.append(year_1956.split(", "))

    def identify_code_version(self, message):
        for year, alpha in enumerate(self.alphabets):
            if all(word in alpha for word in message):
                return year
        return None

    def dictionnarize(self, year):
        if year not in range(4):
            return None
        new_year = (year + 1) % 4
        return  dict(zip(self.alphabets[year], self.alphabets[new_year]))


class NatoTranslator:
    def __init__(self, message: list):
        self.message = message
        self.alphas = NatoAlphabets()
        self.year = self.identify_version()
        self.translator = self.get_translator()
        self.output = self.translate_message()

    def identify_version(self):
        return self.alphas.identify_code_version(self.message)
    
    def get_translator(self):
        return self.alphas.dictionnarize(self.year)

    def translate_message(self):
        output = []
        if self.translator:
            for word in self.message:
                output.append(self.translator[word])
        return output

    def print_output(self):
        print(*self.output)


def main():
    message = input()
    print(message, file=sys.stderr, flush=True)
    translator = NatoTranslator(message.split())
    translator.print_output()


if __name__ == "__main__":
    main()