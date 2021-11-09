class A:
    def m1(self):
        print("THis is a parent1 class")
class B(A):
    def m1(self):
        print("This is a parent2 class")
class C(A):
    def m1(self):
        print("this is a child class object")
class D(B,C):
    def m1(self):
        print("this is a child class")
d=D()
d.m1()
print(D.mro())

