import re
# ############## Matching WhiteSpaces ########
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

# Check for valid first and last name with a space
s = """Toshio Muramatsu"""


if re.search("\w{2,20}\s\w{2,20}", s):
    print("It is a valid full name")
else:
    print("Invalid Full Name")
