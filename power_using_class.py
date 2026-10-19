class Calculator:
    def __init__(self, num):
        self.num = num
        
    def square(self):
        return self.num ** 2
        
    def cube(self):
        return self.num ** 3
        
    def sqrt(self):
        return round(self.num ** 0.5, 3)
    
    @staticmethod
    def hello():
        print("hello User")

n = int(input("Enter a positive number: "))

p = Calculator(n)
print(p.square(), p.cube(), p.sqrt())
p.hello()