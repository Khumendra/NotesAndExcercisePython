import re
# search for ape in the string
# re.search(pattern, string)


string = "The ape was at the apex"
pattern = "ape"

print(re.search(pattern, string))

if re.search(pattern, string):
    print(f" {pattern} found!")

else:
    print(f"{pattern} not found!")


