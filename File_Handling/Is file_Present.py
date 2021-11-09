#we have to use os module to check the availability of file
#we can use os.path.isfile(fname) to check the availability
# import os
# fname=input("enter the file name")
# if os.path.isfile(fname):
#     print("file exists: ",fname)
#     f=open(fname,'r')
#     text=f.read()
#     print("The content of the file is: ")
#     print("*" * 40)
#     print(text)
#     print('*' * 40)
#     f.close()
import os
fname=input("enter the file name")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,'r')
    text=f.read()
    print("the  content of the file is: ")
    print("*"*40)
    print(text)
    print("*"*40)