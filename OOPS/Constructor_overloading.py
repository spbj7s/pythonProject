#constructor overloading is not possible in python
#if we are trying to declare multiple constructor then pvm will always try to consider the last constructor

# class test:
#     def __init__(self):
#         print("zero arg constructor")
#     def __init__(self,x):
#         print("one valued constructor")
#     def __init__(self,x,y):
#         print("two valued constructor")
# # t=test()
# t=test(10)
# t=test(5,3)

#As python is not supporting constructor overloading then how we are going to overcome this problem with the help of python constructor overloading
#Method1:
# class Test:
#     def __init__(self,a=None,b=None,c=None,d=None,e=None):
#         print("Constructor with 0|1|2|3 number of arguments")
# t=Test()
# t=Test(10)
# t=Test(20,30)
# t=Test(20,30,40)
# t=Test(20,30,40,50,60)

#Method2:Variable lenth constructor

class Test:
    def  __init__(self,*args):
        print("constructor with n number of arguments")
t=Test()
t=Test(10)
t=Test(20,30)
t=Test(20,30,40)
t=Test(20,30,40,50,60)




