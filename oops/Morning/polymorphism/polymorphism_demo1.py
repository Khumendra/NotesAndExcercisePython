class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot cannot swim")

class Penguin:
    def fly(self):
        print("Penguin cannot fly")

    def swim(self):
        print("Penguin can swim")


def fly_test(bird):
    bird.fly()

pa = Parrot()
pe = Penguin()

fly_test(pa)
fly_test(pe)

