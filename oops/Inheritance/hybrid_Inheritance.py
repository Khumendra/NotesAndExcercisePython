# Hybrid Inheritance

class A:
    message = "I am from A."

class B(A):
    message = "BBBBBB"


print(B.message)