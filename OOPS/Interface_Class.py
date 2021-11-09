#a class which only contains the abstract method is known as Interface
#interface acts as a prototype of the class and whenever we have a SRS then only we can use interface
from abc import *
class Interface(ABC):
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m2(self):pass
    @abstractmethod
    def m3(self):pass

class Abstract(Interface):
    def m1(self):
        print("This is Abstract method1 ")
    def m2(self):
        print("this is Abstract method2")
class concrete(Abstract):
    def m3(self):
        print("This is a abstract method 3")
c=concrete()
c.m1()
c.m2()
c.m3()