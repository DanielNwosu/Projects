class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def multiply(self,fraction):
        return Fraction(self.num*fraction.num,self.den*fraction.den)

    def divide(self,fraction):
        return Fraction(self.num*fraction.den,self.den*fraction.num)

    def add(self,fraction):
        numerator = self.num * fraction.den + self.den * fraction.num
        denominator = fraction.den * self.den
        return Fraction(numerator,denominator)

    def subtract(self,fraction):
        numerator = self.num * fraction.den - self.den * fraction.num
        denominator = fraction.den * self.den
        return Fraction(numerator,denominator)

    def invert(Fraction):
        return Fraction(Fraction.den,Fraction.num)

    def make_float(self):
        return self.num/self.den

    def set_numerator(self, numerator):
        self.num =  numerator

    def set_denominator(self,denominator):
        self.den = denominator

    def get_numerator(self):
        return self.num
    def get_denominator(self):
        return self.den

    def __str__(self):
        return str(self.num) + '\\' + str(self.den)



F1 = Fraction(1,4)
F2 = Fraction(2,3)

print(F1, ' + ', F2, ' = ', F1.add(F2))
print(F1, ' - ', F2, ' = ', F1.subtract(F2))
print(F1, ' * ', F2, ' = ', F1.multiply(F2))
print(F1, ' / ', F2, ' = ', F1.divide(F2))