#there are two types of files are there
#1.Text files and Binary Files
#Modes of operation of a file r,w,a,r+,w+,a+,x(Exclusive)

# f=open("abc123.txt","x")#New file will be created
# # f=open("abc.txt","x")
# #f=open("abc.txt","r")
# print("file name:",f.name)
# print("file mode",f.mode)
# print("is file closed:",f.closed)
# print("is file readable",f.readable())
# print("is file writable",f.writable())
# f.close()
# print("is file closed",f.closed)

#writing a data to the file
#f.write(str) method:
#f=open('abc.txt','w')
# f=open('abc.txt','a')
# f.write("smruti\n")
# f.write("purna\n")
# f.write("Badajena\n")
# print("write method was successful")
# f.close()

#f.writelines(str) method:

f=open('abc.txt','a')
l=["smruti\n","tapasweeni\n","sradha\n","Rahul\n"]
f.writelines(l)
