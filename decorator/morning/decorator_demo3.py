def print_msg(message):
    greeting = "Hello"

    def display():
        print(greeting, message)
    display()
    

func = print_msg(message="Python is general purpose lang")
# print(func)