# create a class


class Calculator:
    # class attribute
    name = "My Calculator"

    # Constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return None

    # instance method
    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        if self.num2 > self.num1:
            result = self.num2 - self.num1
        else:
            result = self.num1 - self.num2
        return result

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


calc = Calculator(10, 20)

print(

    "\n",    "Number1:", calc.num1,
    "\n",    "Number2:", calc.num2,
    "\n\n",    "Addition:", calc.addition(),
    "\n",    "Subtraction:", calc.subtraction(),
    "\n",    "Multiplication:", calc.multiplication(),
    "\n",    "Division:", calc.division(),
)
