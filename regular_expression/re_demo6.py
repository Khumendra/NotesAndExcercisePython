import re 
# ########### Matching Any Character ##############
# . matches any character. but what if we  want to match a period.
# Backslash the period 
# You do the same with[, ] and others

# Note
# . means any character 
# \. means (.)

randStr = "F.B.I. I.R.S. CIA"


print("Matches :", len(re.findall(".\.\.", randStr)))
print("Matches :", re.findall(".\.\.", randStr))

print("Matches :", len(re.findall(".\..\..", randStr)))
print("Matches :", re.findall(".\..\..", randStr))
