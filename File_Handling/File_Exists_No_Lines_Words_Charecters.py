# import os
#
# fname=input("Enter a file name: ")
# if os.path.isfile(fname):
#      print("File exists",fname)
#      f=open(fname,'r')
#      lcount=wcount=ccount=0
#
#      for line in f:
#          lcount=lcount+1
#          word_count_Current_line=len(line.split())
#          wcount=wcount+word_count_Current_line
#          ccount=ccount+len(line)
#
#      print(lcount)
#      print(wcount)
#      print(ccount)
# else:
#     print("File doesnt exist")
# import os
# fname=input("enter the file name: ")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     f=open(fname,'r')
#     lcount=0
#     wcount=0
#     ccount=0
#     for line in f:
#         lcount=lcount+1
#         wcount=wcount+len(line.split())
#         ccount=ccount+len(line)
#
#     print(lcount)
#     print(wcount)
#     print(ccount)
# else:
#     print("File doesnot exist")


#Practice
import os
fname=input("enter a file name: ")
if os.path.isfile(fname):
    print("file exists",fname)
    f=open(fname,"r")
    lcount=wcount=ccount=0
    for line in f:
        lcount=lcount+1
        wcount=wcount+len(line.split())
        ccount=ccount+len(line)

    print(lcount)
    print(wcount)
    print(ccount)

else:
    print("file didnt exists")


