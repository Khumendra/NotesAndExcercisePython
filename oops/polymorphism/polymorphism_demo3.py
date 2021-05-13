# Duck-Typing


class VisualStudioCode(object):
    def execute(self):
        print("Compiling...")
        print("Running...")


class PyCharm:

    def execute(self):
        print("Compiling...")
        print("Running...")
        print("Convention check.")
        print("Spell Check.")


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = VisualStudioCode()
ide = PyCharm()

laptop = Laptop()

laptop.code(ide)
