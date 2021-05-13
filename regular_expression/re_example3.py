import re


# for i in re.finditer("ape.", theStr):
#     # Span returns a tuple
#     locTuple = i.span()
#     print(locTuple)

#     # Slice the match out using the tuple values
#     print("#", theStr[locTuple[0]: locTuple[1]])


string = "The ape was at the apex"
pattern = "ape."

iterObj = re.finditer(pattern, string)

# print(list(iterObj))

for i in iterObj:
    loc = i.span()
    print(loc, end=' ')

    print(
        string[loc[0]:loc[1]]
    )
