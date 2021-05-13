# passing any function as an argument

def greet():
    return "Hello There!"

def other(func):
    print("Calling function...")
    print(func())

other(func=greet)