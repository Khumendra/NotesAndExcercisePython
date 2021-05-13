# Single Inheritance
# One Class - Other Class


class Fruit:
    def __init__(self):
        print("I am a fruit")

    def message(self):
        print("message from fruit")


class Citrus(Fruit):
    def __init__(self):
        super().__init__()
        print("I'm citrus")

    def message(self):
        print("message from Citrus fruit")


lemon = Citrus()
lemon.message()
