#WAP to find a numbe ri sprime number or not
# n=int(input("enter a number: "))
# n1=2
# while n1<n:
#     is_prime=True
#     for i in range(2,n):
#         if (n1%i)==0:
#             is_prime=False
#             break
#     if is_prime==True:
#         print(n)
#         n1=n1+1
# Python program to display all the prime numbers within an interval

# lower=1
# upper=100
# print("prime number between {} and {} are".format(lower,upper))
# for num in range(lower,upper+1):#1,2,3,4,
#     #print(num)
#     if num>1:
#         for i in range(2,(num//2)+1):
#             #print(i)
#             if(num%i==0):
#                 break
#         else:
#             print(num)


a=[]
# lower=1
# upper=100
# print("print the prime numbers beween{} and {}".format(lower,upper))
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i==0):
#                 break
#         else:
#             print(num)
#             a.append(num)
# print(a)

# a=[]
# lower=1
# upper=100
# print("print the prime numbers in between{} to {}".format(lower,upper+1))
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)
#             a.append(num)
# print(a)

#WAP to check wheather a number is a prime number or not
# n=int(input("enter a number: "))
# if n<=1:
#     print("The number is not a prime number")
# else:
#     is_prime=True
#     for i in range(2,n):
#         if (n%i)==0:
#             is_prime=False
#             break
#
#     if is_prime==True:
#         print("It is a prime Number")
#     else:
#         print("not a prime number")

# lower=10
# upper=50
# a=[]
# print("display the prime number in between {} to {}".format(lower,upper))
# for n in range(lower,upper+1):
#     if n>1:
#         for i in range(2,n):
#             if(n%i)==0:
#                 break
#         else:
#             a.append(n)
# print(a)
# n=int(input("Enter a number: "))
# if n<1:
#     print("its not a prime number")
# else:
#     is_prime=True
#     for i in range(2,n):
#         if(n%i)==0:
#             is_prime=False
#             break
#     if is_prime==True:
#         print("its a prime number")
#     else:
#         print("is not a prime number")

#Prime Number practice
# n=int(input("enter a number: "))
# if n<=1:
#     print("its not a prime number")
# else:
#     is_prime=True
#     for i in range(2,n):
#         if(n%i)==0:
#             is_prime=False
#             break
#     if is_prime==True:
#         print("its a prime number")
#     else:
#         print("its not a prime number")

#Prime number between a range

lower=int(input("Enter the lower range: "))
upper=int(input("Enter the lower range: "))
a=[]
print("print the prme number between {} to {} ".format(lower,upper))
for n in range(lower,upper+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            a.append(n)
print(a)