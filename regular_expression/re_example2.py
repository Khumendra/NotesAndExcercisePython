import re
# re.findall(pattern, string)
# (.) is used to match any 1 character or space.

# allApes = re.findall("ape", "The ape was at the apex")
# # allApes = re.findall("ape.", "The ape was at the apex")

# for i in allApes:
#     print(i)

string = "The ape was at the apex"

pattern = "ape."


allApe = re.findall(pattern, string)

print(
    *allApe, sep='\n'
    
    )