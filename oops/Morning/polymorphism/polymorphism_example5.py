class Penguin(object):
    def fly(self):
        print("Penguin can not fly! ")

    def swim(self):
        print("Penguine can swim!")


class Parrot:
    def fly(self):
        print("Parrot can  fly! ")

    def swim(self):
        print("Parrot can not swim!")

# interface for executing method
def test(bird):
    bird.fly()
    bird.swim()


parrot = Parrot()
penguin = Penguin()

test(bird=parrot)
test(bird=penguin)
