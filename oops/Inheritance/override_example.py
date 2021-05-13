class Parent(object):
    def greet(self):
        print("Good Morning Kid!!!")

class Child(Parent):
    def greet(self):
        print("Good Morning A!!")
        

child = Child()
child.greet()




