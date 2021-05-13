print("="*40)

def greet(func):
    def inner_func():
        print("Good Question")
        func()
    return inner_func

@greet
def hello():
    print("Hello World!!!")




hello()


