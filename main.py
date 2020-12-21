class fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def simplify(self):
        if self.num >= self.den:
            limit = self.num
        else:
            limit = self.den
        for x in range(1, limit):
            if self.num % x == 0 and self.den % x == 0:
                gcf = x
        self.num = int(self.num / gcf)
        self.den = int(self.den / gcf)

    def printFraction(self):
        self.simplify()
        print("/".join([str(self.num), str(self.den)]))


f = fraction(int(input("Enter the numerator:")),int(input("Enter the denominator")))
f.printFraction()
