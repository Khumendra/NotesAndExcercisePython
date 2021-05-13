# create class
class Dog(object):
    # class attribute
    species = "Lab"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "some sound"

    # Instance method
    def description(self):
        return f'{self.name} is {self.age} years old'

    # Instance method
    def speak(self):
        self.sound = sound
        return f'{self.name} says {sound}'

    def print_sound(self):
        print(self.sound)

# object
miles = Dog("Miles", 4)

# destructor
# del miles


# print(miles.species)
# print(
#     miles.speak("woof woof"), "\n",
#     miles.description()
# )

miles.print_sound()
