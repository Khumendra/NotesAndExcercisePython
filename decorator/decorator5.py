# Passing any function as an argument


def greet():
    return 'Hello There!'


def other(func):
    print("calling other function...")
    print(func())

other(func=greet)
