def addition(num1, num2):
    print(__name__)
    return num1 + num2


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
    


# Entry point in python
if __name__ == '__main__':
    print( 'Addition:',addition(10, 50))