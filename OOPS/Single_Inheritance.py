class parent:
    def m1(self):
        print("This is a parent method")
class child(parent):
    def m2(self):
        print("this is child class method")
c =child()
c.m1()
c.m2()