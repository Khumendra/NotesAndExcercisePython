# Overriding: subclass may change the functionality of a python method in the superclass


class A:
    def say_hi(self):
        print("I'm in A")


class B(A):
    def say_hi(self):
        print("I'm in B")

obj_b = B()
obj_b.say_hi()

