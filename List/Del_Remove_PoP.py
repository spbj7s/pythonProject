#Delete operation:
#Delete will remove the particular element and

# l=[1,2,3,4,5]
# del l[1]
# print(l)
# # del l[2:]
# print(l)
# del l[::]
# print(l)
# list
#Remove will erase particular element from the list
# l=[1,2,3,5,6]
# l.remove(2)
# print(l)
# #Pop operation
# l.pop(3)
# print(l)

# l=[[1,8],[1,2,3,4],[1,2,6,7]]
# #op l=[1,2,3,4,6,7]
# ol=[]
# for nl in l:
#     print(nl)
#     if i not in nl:
#         ol.append(i)
#
# #for i in nl:
# #if  not in i:
# #ol.append(i)
# ns=set(ol)
# lp=list(ns)
# print(lp)

#Remove the element form the list and print the element after removal

# l=[1,2,3,4,5,6]
# print("print the list before removal: ",l)
# x=int(input("Enter the element in the   list to remove: "))
# if x in l:
#     l.remove(x)
#     print("Display the list after removing the element: ",l)
# else:
#     print("The element {} is not present in the list: ",x)

#Remove the element form the list and print the element after removal by using inifinty loop

l=[1,1,1,2,3,3,4,4,5,5,3,3,6,7,7,8,8]

x=int(input("enter the element to be removed :"))

while True:

    if x in l:
        l.remove(x)
    else:
        break
print("the new list is: ",l)

