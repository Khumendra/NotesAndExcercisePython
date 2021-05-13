name = 'makku'

name_number = []

for x in name:
    # print(
    #     ord(x),
    # )
    name_number.append(ord(x))

print(name_number)

for x in name_number:
    print(
        chr(x), end=''
    )
