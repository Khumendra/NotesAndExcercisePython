print()
import re 
# search for ape in the string
# re.search(pattern, string)

if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

print(end='\n\n')

# re.findall(pattern, string)
# (.) is used to match any 1 character or space.

allApes = re.findall("ape", "The ape was at the apex")
# allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

print(end='\n\n')
# re.finditer(pattern, string)
# returns an iterator of matching objects
# you can use span to get the location

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
    # Span returns a tuple
    locTuple = i.span()
    print(locTuple)
    
    # Slice the match out using the tuple values
    print("#",theStr[locTuple[0]: locTuple[1]])