import re
# ########## Matching One or More ##############
# + matches 1 or more characters

# Match a followed by 1 or more characters
print("Matches:", len(re.findall("a+", "a as  ape bug")))
print("Matches:", re.findall("a+", "a as  ape bug"))

