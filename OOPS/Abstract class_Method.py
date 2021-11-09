# #its is atype of class which didnt have  any implementation but for future implementation we hav eto declare such type of classes
# #it is basically present in abc module
# #every abstract class is the child of ABC(Abstract Base Class) parent class
# #Every parent abstract class is going to be implemented in child class
#
# #EX1:
#
# from abc import ABC,abstractmethod
# class vechicle(ABC):
#     @abstractmethod
#     def getnowheels(self):
#         pass
#
# class bus(vechicle):
#     def getnowheels(self):
#         return 4
# class auto(vechicle):
#     def getnowheels(self):
#         return 3
# b=bus()
# print(b.getnowheels())
# a=auto()
# print(a.getnowheels())

#Important conclusion
#if a abstract method is declared in the parent class it is compulsory to declare the implemention of the abstract class in the child class
#lets take some of the below valid and invalid scenarios to check
#Scenario-1
# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):pass
# class subtest(Test):pass
#
# s=subtest()
#it will show an error because we are not implementing the parent class in child class
#Scenario-2:
# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):pass
#     @abstractmethod
#     def m2(self):pass
# class subtest(Test):
#     def m1(self):
#         print("this is the implementation of first abstarct class")
# s=subtest()

#TypeError: Can't instantiate abstract class subtest with abstract method m2
#we will be getting the above error as we are declaring two abstarct method in parent class but only implementing
#the first abstract method not the second abstract method,so in that scenario we will get an error
#so for proper implemention we have to declare the implementtaion for both the abstract methods

#Scanrio-3

# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):pass
#     @abstractmethod
#     def m2(self):pass
# class subtest(Test):
#     def m1(self):
#         print("this is the implementation of first abstarct class")
#     def m2(self):
#         print("this is the implementation of second abstarct class")
# s=subtest()
# s.m1()
# s.m2()

#the above senario will work as required because the parent class abstract method is implemented in child class
#so it will not through any error

#Scenario-4

from abc import *
class Test(ABC):

    def m1(self):pass
    @abstractmethod
    def m2(self):pass
class subtest(Test):
    #def m1(self):
        #print("this is the implementation of first abstarct class")
    def m2(self):
        print("this is the implementation of second abstarct class")
s=subtest()
s.m1()
s.m2()

