# How to overload a function


def add(instanceOf, *args):
    if instanceOf == "int":
        result = 0
    if instanceOf == "str":
        result = ""

    for i in args:
        # result = result+i
        result += i

    return result


print(
    add("int", 3, 4, 5,),
    add("str", "hello", " ", "world"), sep='\n'
)
