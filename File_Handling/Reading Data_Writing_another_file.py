# f1=open("abc.txt",'r')
# f2=open("abc12.txt",'w')
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()
# print("data copied to the file successfully")

#Practice:
# f1=open("abc.txt",'r')
# f2=open("abc12.txt",'w')
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()
# print("data copied successfully")
#WAP to append the content of one file to another file
fname1=input("enter the file to be read from: ")
fname2=input("enter the file to be append: ")
f1=open(fname1,'r')
data=f1.read()
f1.close()
f2=open(fname2,'a')
f2.write(data)
f2.close()
