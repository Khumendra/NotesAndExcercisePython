# from calculator import (addition,
#                         subtraction,
#                         multiplication,
#                         division)

from calculator import (addition as add,
                        subtraction as sub,
                        multiplication as mul,
                        division as div)

from calculator import *

from greet import greet


num1 = 10
num2 = 20

print(
    add(num1, num2),
    sub(num1, num2),
    mul(num1, num2),
    div(num1, num2),
    sep='\n'
)

print(
    greet("Makku")
)
