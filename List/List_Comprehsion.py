#Creation of list elemnts with Square values form 1 to 10
#
# l=[x*x for x in range(1,11)]
# print(l)
# O/p:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# l=[2**x for x in range(1,5)]
# print(l)
# o/p:[2, 4, 8, 16]

# l=[x for x in range(1,91) if x%10==0]
# print(l)

#I/P: words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
#Output: ['B', 'N', 'V', 'C']
# words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
# l=[word[0] for word in words]
# print(l)
# num1=[10,20,30,40]
# num2=[30,40,50,60]
# l=[i for i in num1 if i not in num2]
# print(l)
# l=[i for i in num1 if i in num2]
# print(l)
# words="the quick brown fox jumps over the lazy lazy dog"
# word=words.split()
# w=0
# print(word)
# output=[[i.upper(),len(i),] for i in word if i in words ]
# print(output)

# #Output
# ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# [['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4],
# ['THE', 3], ['LAZY', 4], ['DOG', 3]]
str="blue green black blue green green"
word=input("enter a word to search: ")
c=0
a=[]
a=str.split()
print(a.sort())
b=set(a)
print(a)
print(b)
for i in range(0,len(a)):
    if(word==a[i]):
        c=c+1
print("The number of occurance of the word is: ",c)

# Q) Write a Program to display Unique Vowels present in the
#  given Word

# vowels=['a','e','o','u','i']
# words=input("Enter a word to find out the Vowels: ")
# result=[]
# for ch in words:
#     if ch not in vowels:
#         result.append(ch)
#     else:
#         print("vowels are:",vowels)
# print(len(result))

# l=[ch for ch in words if ch not in vowels]
# print("number of consonents present are:",len(l))
