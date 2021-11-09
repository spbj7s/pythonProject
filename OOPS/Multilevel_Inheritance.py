class Grandparent:
    def m1(self):
        print("This is a Grand parent method")
class Parent(Grandparent):
    def m2(self):
        print("this is parent method")
class child(Parent):
    def m3(self):
        print("child class method")
c =child()
c.m1()
c.m2()
c.m3()
