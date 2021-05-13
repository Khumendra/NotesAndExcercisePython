# write a file

with open('file.txt', 'w') as file:
    # print(file.writable())
    lines = [
        "Python is awesome",
        "\n Js is also my favorite lang"
    ]
    file.writelines(lines)
