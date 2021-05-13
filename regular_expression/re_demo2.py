import re
print()

################# match 1 of Several Letters ################
# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties unless they are listed

animalStr = "Cat rat mat fat pat"

allAnimals = re.findall("[crmfp]at", animalStr)

for i in allAnimals:
    print(i)



print()

# we can also allow for characters in a range
# Remember to include upper and lowercase letters
animalStr = "Cat rat mat fat pat"
someAnimals = re.findall("[c-mC-M]at", animalStr)

for i in someAnimals:
    print(i)




