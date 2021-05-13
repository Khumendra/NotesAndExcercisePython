# Abstraction: process of hiding the real implementation of an application from the user
# providing the essential features to the user
# efficiency and reduce the complexity

# Abstract Class: which has atleast one abstract method
# Abstract Method: which don't have body.
from abc import ABC, abstractmethod


# abstract class
class ParentClass(ABC):

    # abstract methods
    @abstractmethod
    def message(self):
        pass

    def message2(self):
        print("Message from Parent Class.")


class ChildClass(ParentClass):
    def message(self):
        print("Message from Child Class.")
    
    def show(self):
        print("Showing...")
    

# parent = ParentClass()
child = ChildClass()
child.message()
child.message2()
child.show()
