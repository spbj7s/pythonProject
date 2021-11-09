f=open('abc.txt','r')
list=f.readlines()
print(list)

print(f.tell())
print(f.seek(0))
print(f.tell())
print(f.seek(10))
print('the index of the vaue is:',f.tell())
print("is file is closed: ",f.closed)
# for words in list:
#     print(words,end='')
f.close()
