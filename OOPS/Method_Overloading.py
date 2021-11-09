#Method overloading is not possible in python
#the latest method will consider as the resulted method for calling the method


# class Test:
#     def m1(self):
#         print("this a parent class method1")
#     def m1(self,x):
#         print("this is parent class method2 ")
#     def m1(self,x,y):
#         print("this is parent class method 3")
# t=Test()
# t.m1(10,20)

#Example 2

class Test:
    def m1(self,*args):
        # print("this is smruti")
        sum_total=0
        for i in args:
            sum_total=sum_total+i
        print("sum of the number is :",sum_total)

t=Test()
t.m1()
t.m1(10)
t.m1(20,30,40)
t.m1(5,7,8.3,9.5)

