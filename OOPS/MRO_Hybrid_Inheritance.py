class A:
    def m1(self):
        print("THis is a parent1 class")
class B:
    def m1(self):
        print("This is a parent2 class")
class C:
    def m1(self):
        print("this is a child class object")
class D(A,B):
    def m1(self):
        print("this is a child class")
class E(B,C):
    def m1(self):
        print("THis is a parent1 class")
class F(D,E,C):
    def m1(self):
        print("THis is a parent1 class")
f=F()
f.m1()
print(F.mro())
print(D.mro())
print(E.mro())
print(B.mro())
print(A.mro())
print(C.mro())


