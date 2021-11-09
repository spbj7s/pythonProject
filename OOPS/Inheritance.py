# class Car:
#     def __init__(self,carname,brand,color):
#         self.caraname= carname
#         self.brand=brand
#         self.color=color
#     def carinfo(self):
#         print("\t display the car name is {}\n,\tand brand is {}\n,\t car color is{}\n".format(self.caraname,self.brand,self.color))
#
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def Perinfo(self):
#         print("all the persons do eating and drinking")
# class employeee(person):
#     def __init__(self,name,age,sal,empid,car):
#         super(employeee, self).__init__(name,age)
#         self.sal=sal
#         self.empid=empid
#         self.car=car
#     def showempdata(self):
#         print("{}\nis {} old\nand his emp is id {}\nhe is getting salary of {}\n".format(self.name,self.age,self.empid,self.sal))
#         self.car.carinfo()
# car=Car("i20","hundai","black")
# emp=employeee("smruti",28,85000,848460,car)
# emp.showempdata()
# emp.Perinfo()

class car:
    def __init__(self,carname,brand,color):
        self.carname=carname
        self.brand=brand
        self.color=color
    def carinfo(self):
        print("\tcar name is{}\n,The brand name is{}\n,The color is{}\n".format(self.carname,self.brand,self.color))

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def perinfo(self):
        print("All the person are drinking and eating")
class employee(person):
    def __init__(self,empno,name,age,sal,car):
        super(employee, self).__init__(name,age)
        self.empno=empno
        self.age=age
        self.sal=sal
        self.car=car

    def showempdata(self):
        print("The emp name is{},age is {},Emp number is{},Salary is {}".format(self.name,self.age,self.empno,self.sal))
        self.car.carinfo()
c=car("i20","Hyundai","black")
emp=employee("smruti",28,848460,38000,car)
emp.showempdata()
emp.perinfo()
