#Number of charecter occurence present in the given string without count menthod

# s='ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEEF'

# s=input("enter a string to check for the duplicacy: ")
# d={}
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# #print(d)
# for i,j in sorted(d.items()):
#     print("{} occurs {} many times".format(i,j))

# Write the program for the following requirement:
#  Input: ABAABBCA
#  Output: 4A3B1C

# s=input("enter the input string")
# d={}
# output=""
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()):
#
#     output=output+k+str(v)
# print(output)

s=("enter the input string: ")
d={}
output=" "
for ch in s:
    d[ch]=d.get(ch,0)
print(d)
for k,v in sorted(d.items()):
    print("the letter {} accurs this many time{}".format(k,v))


#Write a program to find the number of occurrences of each
#vowel present in the given string?

# s=input("enter a string to search the vowel")
# v=['a','e','i','o','u','A','E','I','O','U']
# d={}
# for ch in s:
#     if ch in v:
#         d[ch] = d.get(ch, 0) + 1
# for k,v in sorted(d.items()):
#     print('{} occurs {} times'.format(k,v))

#Write a program to check whether the given two strings are
#anagrams or not?

# s1=input("enter first string")
# s2=input("enter second string")
# if sorted(s1)==sorted(s2):
#     print("The strings are Anagrams")
# else:
#     print("The strings are not Anagrams")

#sTRING pALLINDROM

# s=input("enter a string")
# if s==s[::-1]:
#     print("string Pallindrom")
# else:
#     print("Not Pallindrom")

#3 string program

# s1=input("enter the first string")
# s2=input("enter the second string")
# s3=input("enter the third string")
#
# i=j=k=0
#
# while i<len(s1) or j<len(s2) or k<len(s3):
#     output=""
#     if i<len(s1):
#         output=output+s1[i]
#         i=i+1
#     if j<len(s2):
#         output=output+s2[j]
#         j=j+1
#     if k<len(s3):
#         output=output+s3[k]
#         k=k+1
# print(output)

# s=input("enter a string").upper()
# d={}
# output=""
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# print(d)
# for k,v in sorted(d.items()):
#     #print("{} occurs {} times in the list".format(k,v))

#     output=output+str(v)+" "+ k
# print(output)

s=input("enter a string")
d={}
output=""
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
for k,v in d.items():
    output=output+str(v)+k
print(output)





