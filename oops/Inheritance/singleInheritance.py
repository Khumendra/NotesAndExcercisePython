# The super() function is used to give access to methods and properties of a parent or sibling class.
# The super() function returns an object that represents the parent class.


class Fruit:
    def __init__(self):
        print("I'm a fruit")

class Citrus(Fruit):
    def __init__(self):
        super().__init__()
        print("I'm citrus")

lemon = Citrus()