# This can be created using very basic method But I am Creating it using Class

class Calculator():
    def __init__(self,num1: int,num2:int):
        self.num1 = num1
        self.num2 = num2
    @property
    def sum(self):
        return f"The Sum of these Numbers is {self.num1 + self.num2}"
    @property
    def sub(self):
        return f"The Subtraction of these Numbers is {self.num1 - self.num2}"
    @property    
    def mul(self):
        return f"The Multiplication of these Numbers is {self.num1 * self.num2}"
    @property
    def div(self):
        return f"The Division of these Numbers is {round((self.num1 / self.num2),2)}"


n1 = int(input("Enter the First Number: "))
n2 = int(input("Enter the Second Number: "))
obj = Calculator(n1, n2)
print(obj.sum)
print(obj.sub)
print(obj.mul)
print(obj.div)
