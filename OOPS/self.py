# class Test:
#     def __init__(self):
#         print("the address of self object is:",id(self))
# s=Test()
# print("the address of the object is:",id(s))
# #Example-2

# class Test:
#     def __init__(self):
#         print("constructor")
#     def m1(self,x):
#         print("print the reference variable:",x)
#
# t=Test()
# t.m1(10)

#is self is a key word in python:self is not a key word  

class Student:
    def __init__(delf,name,age,mark):
        delf.name=name
        delf.age=age
        delf.mark=mark
    def show(kelf,x):
        print("the name of the student is :", kelf.name)
        print("the roll number of the object is:",kelf.age)
        print("the mark of the student is:",kelf.mark)
        print("printthe varibale value in method x:",x)

s = Student("smruti",28,101)

s.show(10)
print(s.name)
print(s.age)
print(s.mark)







