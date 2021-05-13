
import re
# ########## Matching White-Spaces #############
# We can match any white space character

randStr = """This is a long 
string that goes
on for many lines"""

print(
    # randStr

)

# Remove newlines
regex = re.compile("\n")
# print(type(regex))

# print("-----",regex,"-----")

randStr = regex.sub("", randStr)
print(randStr)
