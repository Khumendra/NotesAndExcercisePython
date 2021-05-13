# Creating a class in python


class Animal:
    def __init__(self, species):
        self.__species = species
    
    def sound(self):
        print('Some Sound!!!')

tiger = Animal('Tiger')

print(
    tiger._Animal__species
)