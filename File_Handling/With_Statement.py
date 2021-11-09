#by using with statement we can open a file and we can use this to group file operation with in a block
#The biggest advantage of with statement is it will take care of file automatically once reached to the end of the block it will close the file and even in the case of exception aslo it will close the file automatically.
#we dont have to write block of code to close the file
#syntax is:
#with open (filename,'r') as f:
#.....block of code............

with open('abc.txt','r') as f:
    print(f.read())
with open('abc.txt', 'w') as f:
    f.write("smrutipurna\n")
    f.write("Badajena")
    print("is file is closed",f.close())
print("is file closed",f.close())
