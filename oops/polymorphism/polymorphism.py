# polymorphism


class Dog(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'



dog = Dog('dog')
cat = Cat('cat')

print()

print(dog.speak())
print(cat.speak())



