class parent1:
    def m1(self):
        print("THis is a parent1 class")
class parent2:
    def m1(self):
        print("This is a parent2 class")
class child(parent1,parent2):
    def m3(self):
        print("this is a child class object")
c=child()
c.m1()
c.m3()
