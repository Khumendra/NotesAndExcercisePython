class Fruit:
    def __init__(self):
        print("I am a Fruit!")


class Citrus(Fruit):
    def __init__(self, first_name, last_name):
        super().__init__()
        print("I am Citrus!")


lemon = Citrus()
