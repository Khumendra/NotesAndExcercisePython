class Computer:
    def __init__(self):
        # self.__updateSoftware()
        # self._driver()
        return None

    def _driver(self):
        print('driving...')

    def __updateSoftware(self):
        print("Updating Softwares...")


laptop = Computer()
laptop._driver()

# name mangling
laptop._Computer__updateSoftware()