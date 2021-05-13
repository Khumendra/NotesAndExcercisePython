import re

# ######## Matching Any single Letter or Number ############
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]

phNum = "412-555-1212"

 

# Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

# Check for valid first name between 2 and 20 characters
s = "John Doe"
if re.search("\w{2,20}", s):
    print("It is a valid name")