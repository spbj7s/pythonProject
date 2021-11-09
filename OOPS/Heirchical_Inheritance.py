class parent:
    def m1(self):
        print("THis is a parent class")
class child1(parent):
    def m2(self):
        print("This a child class")
class child2(parent):
    def m3(self):
        print("this second child class")
c1=child1()
c1.m1()
c1.m2()
#c1.m3()