def add(instaceOf, *args):
    if instaceOf == "int":
        result = 0
    if instaceOf == "str":
        result = ""

    for i in args:
        result += i
    return result


print(
    add('int', 1, 2, 3)
    # add('str', 'makku', '@', 'gmail.com')
)
