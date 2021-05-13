def hello(name="makku"):
    print("The hello() func has been executed!")

    def greet():
        return "\t This is the greet() inside hello!"

    def welcome():
        return "\t This is welcome() inside hello!"

    print("I am going to return a function!")

    if name == "makku":
        return greet()

    else:
        return welcome()


f = hello("makku")

print(
    f

)
