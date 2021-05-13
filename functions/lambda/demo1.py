
def mul(num1):
    return (lambda num2: num1*num2)

number = mul(10)

print(
    number(5)
)

