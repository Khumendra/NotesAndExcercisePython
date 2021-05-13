import re
# ########## Matching Multiple Number ###########
# You can match multiple digis by following the \d with {numOfValues}

# Match 5 numbers only

# if re.search("\d{5}", "12345"):
# if re.search("\d{5}", "12345char"):
# if re.search("\d{5}", "char12345"):
if re.search("\d{5}", "1char2345"):
    print("It is a zip code")
else:
    print("Not a zip code")
# You can also match within a range
# Match values that are between 5 and 7 digits
numStr = "123 1234 12345 123456 1234567 12345678"

print("Matches:", len(re.findall("\d{5,7}", numStr)))
print("Matches:", re.findall("\d{5,7}", numStr))
# print("Matches:", re.findall("\d{5, 7}", numStr))
