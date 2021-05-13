import re

string = " DOB is 5-12-1998"
# string = " DOB is 05-12-1998"

match = re.search(r"(\d+-\d+-\d+)", string)
# match = re.search(r"[\d]{1,2}-[\d]{2}-[\d]{4}", string)
if match:
    print(
        "My date of birth is",
        string[(match.span()[0]):match.span()[1]]
    )
else:
    print("Enter valid date format{dd-mm-yy}")


# match = re.search(r"(\d+-\d+-\d+)", string)

# print(match.group())


# match = re.search(r"[\d]{2}-[\d]{2}-[\d]{4}", string)
