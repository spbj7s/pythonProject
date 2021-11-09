# import re
# username=input("enter username ")
# pattern="[a-zA-Z0-9]+[a-zA-Z]+\.(com|net|in)"
# if(re.search(pattern,username)):
#     print("valid email address")
# else:
#     print("invalid email address")

import re
username=input("Enter a pattern: ")
#pattern="[a-zA-Z0-z]+[a-zA-z]+\.(com|net|in)"
pattern="ab"
if (re.search(pattern,username)):
    print()
    print("valid email address")
else:
    print("invalid email adress")
#WAP to check validity of a password

# import re
# s=input("enter a password")
# x=True
# while x:
#     if (len(s)<6 or len(s)>12):
#         break
#     elif not re.search("[a-z]",s):
#         break
#     elif not re.search([0-9],s):
#         break
#     elif not re.search("[A-Z]",s):
#         break
#     elif not re.search("[$#@]",s):
#         break
#     elif not re.search("\s",s):
#         break
#     else:
#         print("valide password")
#         x=False
#         break

#WAP to match a group of item and then show tthe start index and end index in the string
# import re
# count=0
# #pattern = re.compile("ab")
# matcher = re.finditer('ab',"ababaaabbbababab")
# for m in matcher:
#     count =count+1
#     print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
# print('The number of occurences:',count)

#Mached Function:

# str="dhsufdsfAAGG12@gmail.com"
# import re
# matched = re.finditer("[a-z]","dhsufdsfAAGG12@gmail.com")
# matched = re.finditer("[A-Z]","dhsufdsfAAGG12@gmail.com")
# matched = re.finditer("[0-9]","dhsufdsfAAGG12@gmail.com")
# matched = re.finditer("[a-aZ-Z]","dhsufdsfAAGG12@gmail.com")
# matched = re.finditer("[a-zA-Z0-9]","dhsufdsfAAGG12@gmail.com")
# matched = re.finditer("[^a-zA-Z0-9]","dhsufdsfAAGG12@gmail.com")
# matched = re.finditer("\W","dhsufds  fAAG G12@ gmail.com")
# for m in matched:
#     print(m.start(),".....",m.group())
# import re
# matched = re.finditer("d{1,2}a*","ddddddddddhsufdsdddddfAsddAGdddG12@gmail.com")
# for m in matched:
#     print(m.start(),".....",m.group())

# matched = re.finditer("[^d]`","ddddddddddhsufdsdddddfAsddAGdddG12@gmail.com")
# for m in matched:
#     print(m.start(),".....",m.group())
#Match():
import re
s = input("chek the pattern: ")
m=re.match(s,"siamsmrutipurna")
if m!=None:
    print("matched string is present at the begninning")
    print("start index{} of string{}".format(m.start(),m.group()))
else:
    print("string is not matched")

import re
str =input("input a string pattern:")
m = re.findall( "a" ,"aspcvdjfhjdghjd")
if m!=None:
    print("string is not present at the begninng")
    #print("the string index {} for the string {}".format(m.start(),m.group()))
else:
    print("string is present in the beginning")

# import re
# m = re.findall('[0-9]',"as89658")
# print(m)





