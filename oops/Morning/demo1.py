# creating a class
class Dog:
    # Class attribute
    species = "Lab"

    # constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def print_dog(self):
        print('****', self.species, '****')
        print("Dog Name:", self.name)
        print("Dog Age:", self.age)
        


# object
dog_1 = Dog('sammy', 4)
dog_1.print_dog()


