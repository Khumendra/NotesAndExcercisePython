def print_msg(message):
    greeting = "Hello"

    def display():
        print(greeting, message)

    return display


msg = print_msg(message="Python is my favorite lang")
msg()