# Function returning other function


def hello():
    def say_hi():
        return "Hi"
    return say_hi


greet = hello()

print(
    greet()
)
