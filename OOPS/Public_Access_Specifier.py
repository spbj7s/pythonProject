class Test:
    def __init__(self):
        self.x=10
    def m1(self):
        print("it is public method")
    def m2(self):
        print(self.x)
        self.m1()
t=Test()
print(t.x)
t.m2()