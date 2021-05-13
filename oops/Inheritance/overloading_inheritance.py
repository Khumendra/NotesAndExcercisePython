# def add(instaceOf, *args):
#     if instaceOf == 'int':
#         result = 0

#     if instaceOf == 'str':
#         result = ''

#     for i in args:
#         result += i
#     return result


# print(add('int', 3, 4, 5))
# print(add('str', '3', '4', '5'))

class Base:
    def add(self, a, b):
        return a + b


class Derived(Base):
    def add(self, a, b):
        return a + b + 1


base = Base()
derived = Derived()

print(base.add(1, 2))
print(derived.add(1, 2))
