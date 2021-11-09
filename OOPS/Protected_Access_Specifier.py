class Test:
    def __init__(self):
        self._x=10
    def _m1(self):
        print("it is protected method")
    def m2(self):
        print(self._x)
        self._m1()
t=Test()
#print(t._Test__x)
t.m2()