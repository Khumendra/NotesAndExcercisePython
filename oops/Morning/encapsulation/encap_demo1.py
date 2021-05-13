# base class
class Base:
    def __init__(self):
        # protected
        self._a = 10


class Derived(Base):
    def __init__(self):
        # calling constructor of base class
        Base.__init__(self)
        print("Calling...")
        print(self._a)

obj = Derived()
obj2 = Base()

# print(dir(obj))
# print(obj2.a)
print(obj2._a)