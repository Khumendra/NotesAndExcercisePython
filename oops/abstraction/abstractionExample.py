# Abstraction: process of hiding the real implementation of an application from the user
# providing the essential features to the user
# efficiency and reduce the complexity

# Abstract Class: which has atleast one abstract method
# Abstract Method: which don't have body.
from abc import ABC, abstractmethod

# Abstract Class
class Parent(ABC):

    @abstractmethod
    def message(self):
        pass

    
    def message2(self):
        print("I am from Parent Class")


class Child(Parent):
    def message(self):
        print("I am from Child Class")

# obj = Parent()
obj = Child()
obj.message()
obj.message2()