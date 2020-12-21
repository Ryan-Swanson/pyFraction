class fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, rhs):
        self.simplify()
        rhs.simplify()
        gcf = self.den * rhs.den
        self.num *= rhs.den
        rhs.num *= self.den
        self.den = gcf
        rhs.den = gcf
        self.num += rhs.num
        self.simplify()
        return self

    def simplify(self):
        if self.num == self.den:
            self.num = 1
            self.den = 1
            return self

        if  self.num >= self.den:
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
d = fraction(1,2)
f = f + d

f.printFraction()
