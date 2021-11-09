class Parent:
    x=10
    def __init__(self):
        print("this a parent class constructor")
    def m1(self):
        print("this a parent class instance method")
    @classmethod
    def m2(cls):
        print("This is a parent class Class level method")
    @staticmethod
    def m3():
        print("This is a parent class static method")
class child(Parent):
    def __init__(self):
        print("This is a child class constructor")
    def m2(self):
        print("this is a child class  instance method")
    def method1(self):
        print(super().x)
        self.m1()
        super().m2()
        self.m3()
        super().__init__()

c=child()
c.method1()



