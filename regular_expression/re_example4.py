import re

################# match 1 of Several Letters ################
# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties unless they are listed

# animalStr = "Cat rat mat fat pat"

# allAnimals = re.findall("[crmfp]at", animalStr)

# for i in allAnimals:
#     print(i)



string = "Cat rat mat fat pat"
pattern = "[crmfp]at"

allAnimals = re.findall(pattern, string)

print(*allAnimals, sep='\n')




