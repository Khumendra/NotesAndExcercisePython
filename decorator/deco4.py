def print_msg(message):
    greeting = "Hello"

    def printer():
        print(greeting, message)
    
    printer()

print_msg(message="I am good.")
