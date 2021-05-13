import re


########### Solving Backslash Problems ##############
# Regex use the backslash to designate special characters
# and Python does the same inside string which causes issues.

# Let's try to get "\\stuff" out of a string

randStr = "Here is \\stuff"

# This won't find it
print("Find \\stuff :", re.search("\\stuff", randStr))


# This does, but we have to put 4 slashes which is messy
print("Find \\stuff: ", re.search("\\\\stuff", randStr))

# You can get around this by using raw strings which
# don't treat backslashes as special
print("Find \\stuff :", re.search(r"\\stuff", randStr))
# raw string