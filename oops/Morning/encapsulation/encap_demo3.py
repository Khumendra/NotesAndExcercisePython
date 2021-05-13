class Computer:
    def __init__(self):
        self.__updateSoftware()
        self.driver()

    def driver(self):
        print("Driving")

    def __updateSoftware(self):
        print("Updating Software")


laptop = Computer()
# laptop.driver()
laptop._Computer__updateSoftware()