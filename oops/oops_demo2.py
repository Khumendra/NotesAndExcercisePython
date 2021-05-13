# Encapsulation: We can protect the member variables 
# of a class from being accessed by any program outside our class using the principle of Encapsulation.
# _var - private
# __var - protected


# creating a class
class Animal:
    # class-constructor
    def __init__(self, species):
        self._species = species
    
    
    def sound(self):
        if self._species.lower() == "dog":
            print('Barks a lot!')
        elif self._species.lower() == "tiger":
            print("Roars!")
        else:
            print("Silent Animal!")
    def petAnimalTest(self):
        if self._species.lower() == "cat" or self._species.lower() == "cow":
            print("Pet Animal!")
        else:
            print('Lives in Jungle!')
    

# Object creation
animal = Animal('Cat')

animal.sound()
animal.petAnimalTest()



# animal_lives_in_jungle = ["Elephant", "Tiger"]
# pet_animal = ['cat', 'cow', 'horse','dog']
# or 
# # property of animal
# {
#     'cat':"meaow",
#     'dog':'bark'
# }