print("="*50)

def new_decorator(original_func):

    def wrap_func():
        print("Some extra code, before the original function")

        original_func()
        print("Some extra code, after the original function")

    return wrap_func

@new_decorator
def func_need_decorator():
    print("I want to be decorated!")


func_need_decorator()