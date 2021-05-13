def greet(func):
    def wrap_func():
        func()
    return wrap_func()

@greet
def hello():
    print("Hello Good Morning!")