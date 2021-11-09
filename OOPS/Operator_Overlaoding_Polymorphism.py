# # class Book:
# #     def __init__(self,pages):
# #         self.pages=pages
# #     def __add__(self, other):
# #         total_pages=self.pages+other.pages
# #         return total_pages
# # p1=Book(200)
# # p2=Book(300)
# # p3=Book(500)
# # print(p1+p2)
# # print(p1+p3)
# # print(p1+p2)
#
# #operator overloading example 2
#
# # class student:
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
# #     def __gt__(self, other):
# #         return self.marks>other.marks
# #         return self.name>others.name
# #     def __ge__(self, other):
# #         return self.marks>=other.marks
# # s1=student("smruti",100)
# # s2=student("sradha",200)
# # print(s1>s2)
# # print(s1<s2)
# # print(s1>s2)
# # print(s1>=s2)
#
# #operator overloading example3 with multiplication
#
# class emp:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __mul__(self, other):
#         return (self.salary*other.workingdays)
# class timesheet:
#     def __init__(self,name,workingdays):
#         self.name=name
#         self.workingdays=workingdays
#     def __mul__(self, other):
#         return self.workingdays*other.salary
# e=emp("smruti",500)
# t=timesheet("smruti",22)
# print("Salary of the month is: ",e*t)
# print("Salary of the month is: ",t*e)


#Operator overloading example 2 with three operands

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return "the total number of pages is:{}".format(self.pages)
    def __mul__(self, other):
        return Book(self.pages*other.pages)
    def __floordiv__(self, other):
        return Book(self.pages//other.pages)

b1=Book(20)
b2=Book(80)
b3=Book(40)
b4=Book(100)
print(b1+b2+b3)
print(b1*b2+b3)
print(b1+b2//b3)
print(b1*b2+b3*b4)
print(b1*b2+b3//b4)
