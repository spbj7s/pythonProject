class Test:
    def __init__(self):
        self.__x=10
    def __m1(self):
        print("it is private method")
    def m2(self):
        print(self.__x)
        self.__m1()
t=Test()
#print(t._Test__x)
t.m2()