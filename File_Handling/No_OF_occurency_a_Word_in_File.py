fname=input("enter a file name: ")
word=input("eneter the word to be searched: ")
j=0
f=open(fname,'r')
for line in f:
    words=line.split()
    for i in words:
        if(i==word):
            j=j+1
print("occurency of the word: ")
print(j)