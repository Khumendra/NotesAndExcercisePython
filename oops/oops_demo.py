# creating a class

class Dog(object):

    # constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    

my_dog = Dog(name='sammy', breed="Lab")

print(my_dog.name)
print(my_dog.breed)


