# simple calculator

class calculator:
    def __init__(self,a=float,b=float,c=str):
        self.a=a
        self.b=b
        self.c=c.lower()
    def calc(self):
        if self.c == "+":
            return self.a + self.b
        elif self.c == "-":
            return self.a - self.b
        elif self.c == "*":
            return self.a * self.b
        elif self.c == "/":
                return self.a / self.b
            
a=float(input('enter a number'))
b=float(input('enter another number'))
c=input('select a operator')

cal=calculator(a,b,c)
result=cal.calc()
print("answer" ,result)
            
            

        
        