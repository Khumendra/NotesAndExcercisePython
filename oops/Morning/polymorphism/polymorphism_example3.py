class Language:
    def say_hello(self):
        raise NotImplementedError("Please say_hello() in child class")

class Telugu(Language):
    def __init__(self, name):
        self.name = name.title()

    def say_hello(self):
        print(f'{self.name} say: Namashkar')


class English(Language):
    def __init__(self, name):
        self.name = name.title()

    def say_hello(self):
        print(f'{self.name} say: Hello')


def intro(lang):
    lang.say_hello()


telugu = Telugu(name="ramu")
english = English(name="John")

intro(telugu)
intro(english)
