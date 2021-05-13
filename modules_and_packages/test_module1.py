import calculator


num1 = int(input("Number1: "))
num2 = int(input("Number2: "))


# print(calculator.__name__)

print(
    '\n',
    calculator.addition(num1, num2), '\n',
    calculator.subtraction(num1, num2), '\n',
    calculator.multiplication(num1, num2), '\n',
    calculator.division(num1, num2), '\n',

)
