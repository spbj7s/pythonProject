#WAP to take in a string and replace every blank space with hyphens:

# string=input("Enter a string: ")
# string=string.replace(' ','-')
# print("print modified string is: ",string)

#WAP to calculate the length of the string withot using library function

# str=input("enter a string: ")
# c=0
# for i in str:
#     c=c+1
# print("the number of count is: ",c)

#WAP to remove the charecters of odd index vlues ina string
# str=input("enter a string: ")
# output=""
# for i in range(len(str)):
#     if(i%2)==0:
#         output=output+str[i]
# print("the modified string is: ",output)

#WAP to calculate the number of words and the number of charecters present in a string:
# s=input("enter a string: ")
# c=0
# w=1
# for ch in s:
#     c=c+1
#     if(ch==' '):
#         w=w+1
# print(c,w)
#WAP to take two string and display the larger string without using built in function

# s1=input("enter the first string: ")
# s2=input("enter the second string: ")
# c1=0
# c2=0
# for i in s1:
#     c1=c1+1
# for j in s2:
#     c2=c2+1
# if(c1<c2):
#     print("larger string is: ",s2)
# elif(c1==c2):
#     print("Both the strings are equal")
# else:
#     print("larger string is: ",s1)

#WAP to count number of lowercase charecters in a string
# s=input("enter a string: ")
# c=0
# u=0
# for i in s:
#     if(i.islower()):
#         c=c+1
#     else:
#         u=u+1
#
# print("The number of lower case charectersa are:",c)
# print("The number of lower case charectersa are:",u)

#WAP to accept a hyphen separated sequence of words as input and print the words in a hyphen-separated sequence after
#sorting them alphabetically

# s=input("enter a sequence of charecters with hyphen: ")
# list=[i for i in s.split('-')]
# list.sort()
# print('-'.join(list))
#WAP to calculate the number of digits and letters in a string:

# s=input("enter a string: ")
# d=l=0
# for i in s:
#     if(i.isdigit()):
#         d=d+1
#     else:
#         l=l+1
# print("The number of digits are: ",d)
# print("the number of letters are:",l)

#WAP to form a new string made of the first 2 and last 2 charecters from a given string
s=input("enter a string: ")
c=0
for i in s:
    c=c+1
new_string=s[0:2]+s[c-2:c]
print(new_string)