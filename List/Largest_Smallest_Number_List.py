# WAP to find the largest elemnet in the list
a=[]
n=int(input("enter the number of elements: "))
for i in range(1,n+1):
    b=int(input("enter element: "))
    a.append(b)
a.sort
print(a)
print("largest element is: ",a[n-1])

# WAP to find the second largest elemnet in the list

# a=[]
# n=int(input("eneter the number of the element: "))
# for i in range(1,n+1):
#     b=int(input("Enter element: "))
#     a.append(b)
# a.sort()
# print("the second largest number is: ",a[n-2])

# WAP put even and odd elements in alist into two different list

# a=[]
# n=int(input("Enter the number of the element: "))
# for i in range(1,n+1):
#     b=int(input("enter the element: "))
#     a.append(b)
# even=[]
# odd=[]
# for j in a:
#     if(j%2==0):
#         even.append(j)
#     else:
#         odd.append(j)
# print("The eeven list is: ",even)
# print("the odd list is:",odd)
# WAP to merge two lists and sort it
# a = []
# c = []
# n1 = int(input("enter number of elemnts in the list: "))
# for i in range(1, n1 + 1):
#     b = int(input("enter the elements: "))
#     a.append(b)
# n2 = int(input("Enter number of elemnts in the list2: "))
# for i in range(1, n2 + 1):
#     d = int(input("enetr the elements"))
#     c.append(d)
# new = a + c
# new.sort()
# print("The new merged and sorted list is: ", new)
# wap to sort the list according to the second element in sublist

# a = [['a', 21], ['c', 66], ['C', 26]]
# for i in range(0, len(a)):
#     for j in range(0, len(a) - i - 1):
#         if (a[j][1] > a[j + 1][1]):
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j + 1] = temp
# print(a)

#WAP to find out the second largest Number in a list using Bubble Sort

# a=[]
# n=int(input("enter the number element inserted to the list: "))
# for i in range(1,n+1):
#     b=int(input("Enter the element in the List: "))
#     a.append(b)
# for i in range(0,len(a)):
#     for j in range(0,len(a)-i-1):
#         if a[j]>a[j+1]:
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
# print("second largest number is: ",a[n-2])

#WAP to sort a list according to the length of the elemnts
# a=[]
# n=int(input("enter the number of elements : "))
# for i in range(1,n+1):
#     b=input("enter the element: ")
#     a.append(b)
# a.sort(key=len)
# print(a)
#WAP to find the Union of two lists:
# a=[]
# n=int(input("enter the number of elements in the list: "))
# for x in range(0,n):
#     b=int(input("Enter the element "+str(x+1)+":"))
#     a.append(b)
# c=[sum(a[0:x+1])for x in range(0,len(a))]
# print(a)
# print(c)
#WAP to to remove the Duplicate Item from the list

# a=[]
# n=int(input("Enter the number of elemt: "))
# for x in range(0,n):
#     element=int(input("Enter elemnts: "))
#     a.append(element)
# b=set()
# unique=[]
# for x in a:
#     if x not in b:
#         unique.append(x)
#         b.add(x)
# print("Non duplicate element in the list:",unique)