def greet(func):
    def wrap_func():
        print('----------')
        func()
    return wrap_func

@greet
def hello():
    print("Hello Word!!!")

hello()