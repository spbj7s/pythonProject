# l=eval(input("enter a list"))
# print(type(l))

#By Using Range function
# l=list(range(0,10))
# print(l)
# #by using string
# s="smruti"
# l=list(s)
# print(l)

# How to access Nested list

# l=[10, 20, [30, 40]]
# print(l[2][0])

# n=[1,2,3,4,5,6,7,8,9,10]
# print(n[2:7:2])
# print(n[1:8:2])
# print(n[8:1:-2])
# print(n[4::2])
# print(n[4:100])

#List vs Mutability:
# n=[10,20,30,40]
# print(n)
# n[1]=222
# print(n)
# n[2]=22
# print(n)

#Traversing element in the list:

# n=[0,1,2,3,4,5,6,7]
# for i in n:
#     print(i)
# 3)To display only Even Numbers:
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2==0:
#         print(i)
# l = ["A","B","C"]
# x=len(l)
# for i in range(x):
#     print("{} A is available at positive index:{} and at negative index:{}".format(l[i],i,i-x))
# l1=[1,2,3,4,5]
# # eval(input("enter a list1: "))
# l2=[1,2,3]
# # eval(input("enter a list1: "))
# a=[]
# for i in l1:
#     if i in l2:
#         a.append(i)
# print(a)

s='smruti'
v=['a','e','i','o','u']
vow=0
con=0
for ch in s:
    if ch in v:
        vow=vow+1
print(vow)
    # else:
    #     con=con+1
    #     print(con)