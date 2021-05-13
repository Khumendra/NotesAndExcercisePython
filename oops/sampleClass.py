class Dog():
    def __init__(self, breed):
        self.breed = breed

my_sample = Dog(breed = "LAB")

print(type(my_sample))
print(my_sample.breed)

# self: connects the method to the instance of the class and it allows to refer itself.
