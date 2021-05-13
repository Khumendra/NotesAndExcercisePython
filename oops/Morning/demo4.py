
name = "sammy"
age = 3
animal_name = 'dog'
sound = "bow bow!!!"


class Animal:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self, animal_name):
        return f'{self.name} is a {animal_name} and {self.age} years old'

    # Instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'


animal = Animal(name, age)

print(

    "\n", animal.description(animal_name),
    "\n", animal.speak(sound),


)
