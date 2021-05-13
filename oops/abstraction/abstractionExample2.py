from abc import ABC, abstractmethod


# Abstract class
class Computer(ABC):

    # Abstract method
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("It's running.")


class Whiteboard(Computer):
    def write(self):
        print("its writing")

    def process(self):
        print("White Borad")


class Programmer:
    def work(self, comp):
        print("Solving Bugs...")
        comp.process()


# comp = Computer()
lap = Laptop()
prog1 = Programmer()
board = Whiteboard()


# prog1.work(lap)
prog1.work(board)

# comp.process()
# lap.process()
