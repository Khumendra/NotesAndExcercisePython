class Base:
    def __init__(self):
        self.a = "Rohan"
        self.__c ="I'm Safe"

class Derived(Base):
    def __init__(self):
        # calling base class constructor
        Base.__init__(self)
        print('Calling members...')
        print(self._Base__c)
        # print("=====",self.__c)
    

obj = Base()
# print(obj.a)

obj2 = Derived()
# print( dir(obj2))