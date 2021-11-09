# class Test:
#     def __init__(self,name,age,roll):
#         print("constructor is assigning and loading those values in python.............")
#         self.name=name
#         self.age=age
#         self.roll=roll
#     def show(self,x,y):
#         print("print name is:",self.name)
#         print("print age is:",self.age)
#         print("print roll is:",self.roll)
#         print("the value of x and y is:",x,y)
# s1=Test("smruti",25,101)
# print(s1.name,s1.age,s1.roll)
# s2=Test("Rahul",27,300)
# print(s2.name,s2.roll,s2.age)
# s1.show(10,20)
# s2.show(50,60)
# python is mandatory it is always optional
#multiple constructor is possible in python but most recent value is always going to be consider
#constructor overloading is not possible in python
#constructor overloading example:

class Test:

    def __init__(self):
        print("no argument constructor")

    def __init__(self,x):
        print("one argument constructor",x)
# s=Test()
t=Test(20)

#constructor is not manadtory to declare.if we are declaring
#any constructor python is going to provide us a automatic default constructor

class Test:
    def show(self,x):
        print("i am printing the data through default constructor",x)
s=Test()
s.show(10)

