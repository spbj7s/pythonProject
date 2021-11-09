#when a common functionality is required inside a method then rather than calling that function we can create aa method
#we can re use the code that concept is basically called as nested methods

class Test():
    def m1(self):
        def cal(a,b):
            print("the sum of the number is:",a+b)
            print("the product of the number is:",a*b)
            print("the difference is:",a-b)
            print("the avarange is:",(a+b)/2)
        cal(10,20)
        cal(50,60)
        cal(1000,2000)
t=Test()
t.m1()