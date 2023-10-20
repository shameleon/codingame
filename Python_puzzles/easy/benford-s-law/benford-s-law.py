import sys
import math

class BenfordLawFit:
    def __init__(self, n, transactions):
        self.n = n
        self.transactions = transactions
        self.percentage = dict() 
        self.count_digits()
        self.fits_benford_law()
        print('false' if self.fits_benford_law() else 'true')

    def count_digits(self):
        count = dict(zip(range(1, 10), [0] * 9))
        first_digits = ""
        for transaction in self.transactions:
            first_digits += transaction.lstrip('-+0.¥$€£')[0]
        for key, val in count.items(): 
            count[key] = first_digits.count(str(key))
            self.percentage[key] = first_digits.count(str(key)) / self.n

    def fits_benford_law(self):
        benford_law =  {1: 0.301, 2: 0.176, 3: 0.125, 4: 0.097, 5:0.079,
                        6: 0.067, 7: 0.058, 8: 0.051, 9: 0.046}     
        for key, val in self.percentage.items():
            ref = benford_law[key]
            if val < ref - .10 or val > ref + 0.10:
                return False 
        return True


def main():
    n = int(input())
    transactions = [input() for i in range(n)]
    transaction_analysis = BenfordLawFit(n, transactions)


if __name__ == "__main__":
    main()
