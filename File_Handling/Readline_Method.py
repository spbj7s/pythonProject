f=open('abc.txt','r')
# data=f.readline()
# print(data)
# print(f.readline())
# print(f.readline())
# print(f.readline())

#How to read complete file
f=open('abc.txt','r')
line=f.readline()
while line !=" ":
    print(line,end='')
    line=f.readline()
f.close()

#Practice:
f=open('abc.txt','r')
line=f.readline()
while line != " ":
    print(line,end='')
    line=f.readline()
f.close()




