name = 'Vikash'


def say_hello():
    # global name
    name = 'Surya'
    return "Hello " + name


def say_good_evening():
    return "Good Evening " + name


print(
    say_hello(),
    say_good_evening(),
    sep='\n'
)
