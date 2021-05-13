def hello(name="John"):
    print('The hello() func has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'

    # print(greet())
    # print(welcome())

    # print('This is the end of the hello function!')
    print('I am going to return a function!!')

    if name == "John":
        return greet
    else:
        return welcome


# hello()
my_function = hello("")

print(
    my_function()
    
    )