# def fibo_number():
#     a=0
#     b=1
#     while True:
#         yield a
#         b=a+b
#         a = b
#
# f=fibo_number()
#
# for i in range (f):
#     print (f.next())
# # print(next(f))
# # print(next(f))
# # print(next(f))
# # print(next(f))
#WAp to get the Fibonacci Series between 0 to 50
# n=int(input("enter upto the sequence of number upto : "))
# x,y=0,1
# while y<n:
#     print(y)
#     x,y = y,x+y
n=int(input("Enter the sequence upto: "))
x,y=0,1
while(y<n):
    print(y)
    x,y=y,x+y
#WAP that accept a string and calculate the number of didgits and letters
# s =input("input a string: ")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Number of digits are: ",d)
# print("Number of letters are: ",c)
#WAP to count the number of even odd numbers from series of numbers

# numbers=(1,2,3,4,5,6,7,8,9,10,11,12)
# count_odd=count_even=0
# for i in numbers:
#     if (i%2)==0:
#         count_even=count_even+1
#     else:
#         count_odd=count_odd+1
# print("Number of odd numbers are: ",count_odd)
# print("Number of even numbers are: ",count_even)
