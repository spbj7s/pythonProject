n=int(input(("enter number of rows ")))
for i in range(n):
    print((chr(97+i)+" ")*n)

#inverse triangle pyramid

# n=int(input("enter the number of rows "))
# for i in range(n):
#     print("* "*(n-i))

#triangle pyramid

# n=int(input("enter number of rows "))
# for i in range(n):
#     print(" "*(n-i-1) +"* " *(i+1) )

#inverse pyramid

# n=int(input("enter number of rows"))
# for i in range(n):
#     print(' '*i +'* '*(n-i))

#Right Angled Tringle:

# n=int(input("enter number of rows"))
# for i in range (n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# n=int(input("enter the number of rows: "))
# for i in range (n):
#     for j in range(i+1):
#         print("*",end='')
#     print()
# n=int(input("enter the number of rows: "))
# for i in range(n):
#     print(" "*(n-i-1)+"* "*(i+1))

# n=int(input("enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end='')
#     print()
n=int(input("enter the number of row: "))
for i in range(n):
    print("* "*(n-i))