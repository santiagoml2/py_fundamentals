class RationalNumber:
    def __init__(self, numerator: int = 0, denominator: int = 0):

        if isinstance(numerator, int) and isinstance(denominator,int):
            self.numerator = numerator
            self.denominator = denominator
        else:
            self.numerator = int(numerator)
            self.denominator = int(denominator)
    
    '''
    def copy_constructor(self):
        self.denominator = int(self.denominator)
        self.numerator = int(self.denominator)
    '''    
    
    def addition(self):
        return(self.numerator + self.denominator)
    
    def substraction(self):
        return(self.numerator - self.denominator)
    
    def multiplication(self):
        return(self.numerator * self.denominator)
    
    def division(self):
        return(self.numerator / self.denominator)
    
    def __str__(self):
        return (f"Current numerator: {self.numerator } and denominator: {self.denominator}")
    
    def set_values(self):
        self.denominator = int(input("Insert denominator value"))
        print(f"- You said: {self.denominator}")

        self.numerator = int(input("Insert numerator value:"))
        print(f"- You said: {self.numerator}")
    

    
my_number = RationalNumber("8",4)
value = my_number.division()
print(value)
