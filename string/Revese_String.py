# Q2) Write a Program To REVERSE content of the given String by using
#  reversed() function
# 1) input: durga
# 2) output: agrud
#Method1:
str=input("enter a string : ")
output=""
i=len(str)-1
while i>=0:
    output=output+str[i]
    i=i-1
print("Reversed string is: " ,output)

#Method-2:
# str=input("enter a string : ")
# output=str[::-1]
# print("Reversed string is: " ,output)


# Method-3:

# str=input("enter a string")
# s=reversed(str)
# output="".join(s)
# print(output)