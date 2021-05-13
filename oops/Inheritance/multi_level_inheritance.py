# Multi-level Inheritance
class GrandParent:
    grand_msg = "I am your Grand Parent!"
    message = "Grand Parent!"


class Parent(GrandParent):
    parent_msg = "I am your Parent!"
    message = "Parent!"
    

class Child(Parent):
    msg = "I am child!"
    message = 'Child!'


child_obj = Child()

print(
    # child_obj.grand_msg, '\n',
    # child_obj.parent_msg, '\n',
    # child_obj.msg
    child_obj.message
)
