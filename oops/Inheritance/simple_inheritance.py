class Parent:
    def msg(self):
        return "I am from Parent Class!"


class Child(Parent):
    def child_msg(self):
        return "I am kid!"



child_obj = Child()

print(
    child_obj.msg()
    
    )