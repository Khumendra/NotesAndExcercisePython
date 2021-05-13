import re
# ########## Match Any Sigle Number ############
# \d can be used instead of [0-9]
# \D is the same as [^0-9]

randStr = "some random 1234" 
print(
        "\n","Matches:", len(re.findall("\d", randStr)),
        re.findall("\d", randStr),
        # re.findall("[0-9]", randStr),

        "\n","Matches:", len(re.findall("\D", randStr)),
        re.findall("\D", randStr),
        # re.findall("[^0-9]", randStr)


)