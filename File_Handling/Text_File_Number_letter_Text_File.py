#Python program that reads a text file and counts the number of times a
# certain letter appears in the text file
#
# fname=input("enter a file to be searched: ")
# l=input("enetr a word to be be searched: ")
# k=0
# f=open(fname,'r')
# for line in f:
#     words=line.split()
#     for i in words:
#         for letter in i:
#             if(letter==l):
#                 k=k+1
# print("the number of occurence of the word is:",k)

#Python program to read a text file and print all the numbers present in the text file

# fname=input("enter a file name: ")
# f=open("abc12.txt",'r')
# for line in f:
#     words=line.split()
#     for i in words:
#         for letter in i:
#             if(letter.isdigit()):
#                 print(letter)

#WAP to count the number of blank spaces in a text file:

# fname=input("enter  a file name: ")
# k=0
# with open(fname,'r') as f:
#     for line in f:
#         words=line.split()
#         for i in words:
#             for letter in i:
#                 if(letter.isspace):
#                     k=k+1
# print("the number of blank lines are:",k)

#WAP to read a file and capitalize the first letter of every word in the file

fname=input("enter the file name: ")
with open(fname,'r') as f:
    for line in f:
        l=line.title()
        print(l)



