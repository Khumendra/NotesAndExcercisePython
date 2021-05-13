# abstract class
class Language:
    def say_hello(self):    
        print("=+="*50, end='\n')
        raise NotImplementedError("Please use say_hello class in child class.")
        


class Telugu(Language):
    def __init__(self, name):
        self.name = name.title()

    # def say_hello(self):
    #     print(f"{self.name} says: Namashkar")


class English(Language):
    def __init__(self, name):
        self.name = name.title()

    def say_hello(self):
        print(f"{self.name} says: Hello")


def intro(lang):
    lang.say_hello()


ramu = Telugu(name="ramu")
john = English(name="john")

intro(ramu)
intro(john)
