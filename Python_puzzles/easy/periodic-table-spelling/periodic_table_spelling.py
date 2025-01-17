import sys
import math


class PeriodicTable:
    def __init__(self):
        table = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar"
        table += " K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br"
        table += " Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te"
        table += " I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm"
        table += " Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn"
        table += " Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr"
        table += " Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og"
        self.table = table.split()

    def is_element(self, w_struct: dict, l: int)  -> dict:
        if l in [1, 2] and len(w_struct['Tail']) >= l:
            leader = w_struct['Tail'][0].upper()
            if l == 2:
                leader += (w_struct['Tail'][1])
            if l == len(w_struct['Tail']):
                w_struct['Tail'] = None
            else:
                w_struct['Tail'] = w_struct['Tail'][l:]
            if leader in self.table:
                w_struct['Found'] = leader
        return w_struct


class PeriodicTableSpelling:
    def __init__(self, word):
        self.table = PeriodicTable()
        self.word = word
        word_structure = {'Head': '', 'Found': None, 'Tail' : word}
        self.translations = []
        self.splice_by_element(word_structure)
        self.print_result()

    def splice_by_element(self, w_struct: dict):
        if w_struct['Tail'] == None:
            self.translations.append(w_struct)
            return
        result = list([w_struct, w_struct.copy()])
        for i in range(2):
            result[i] = self.table.is_element(result[i], i + 1)
            if result[i]['Found']:
                result[i]['Head'] += result[i]['Found']
                result[i]['Found'] = None
                print("OK", file=sys.stderr, flush=True)
                self.splice_by_element(result[i])
            else:
                print("x", file=sys.stderr, flush=True)

    def print_result(self):
        if self.translations:
            for word_structure in self.translations:
                print(word_structure['Head'])
        else:
            print('none')


def main():
    word = input()
    print(word, file=sys.stderr, flush=True)
    pts = PeriodicTableSpelling(word)
    return


if __name__ == '__main__':
    sys.exit(main())
