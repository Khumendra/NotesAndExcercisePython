# Multiple Inheritance
# A class inherits from multiple classes.

class A:
    pass


class B:
    pass

# order 
class C(A, B):
    pass


c = C()
print(
    isinstance(c, C),
    issubclass(C, A) and issubclass(C, B)
)
