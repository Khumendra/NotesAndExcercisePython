# Encapsulation: We can protect the member variables 
# of a class from being accessed by any program outside our class using the principle of Encapsulation.
# _var - private
# __var - protected



# Creating a class in python
class Animal:
    def __init__(self, species):
        self.__species = species
    
    def sound(self):
        print('Some Sound!!!')

tiger = Animal('Tiger')



print(
    dir(tiger)
    # tiger._Animal__species
    
)