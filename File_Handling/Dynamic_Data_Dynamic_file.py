fname=input("enter file name: ")
f=open(fname,'w')
while True:
    data=input("enter data to write :")
    f.write(data +'\n')
    option=input("Do you want to enter more data Y/N? ")
    if option.lower()=="no":
        break
f.close()
print("data written to the file successfully")

