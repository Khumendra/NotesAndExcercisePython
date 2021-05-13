print()


import re
# Use ^ to denote any character but whatever character are
# between the brackets
animalStr = "Cat rat mat fat pat"
someAnimal = re.findall("[^Cr]at", animalStr)

for i in someAnimal:
    print(i)
print()