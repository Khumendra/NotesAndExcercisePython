import re

# ############### Replace All Matches ##############

# Replace matching items in a string

owlFood = 'rat cat mat pat'

# You can compile a regex into pattern object which
# provide additional methods

regex = re.compile("[cr]at")
# print(dir(regex))

# sub()/substitute replaces items that match the regex in the string
# with the 1st attribute string passed to sub

# regex.sub(repl, string)
owlFood = regex.sub("owl", owlFood)

print(owlFood)
