# str="smruti1"
# output=" "
# i=len(str)-1
# while i<=0:
#     output=output+str[i]
#     i=i-1
# print(output)

# 1) input: Learning Python Is Very Easy
# 2) output: Easy Very Is Python Learning

str="Learning Python656 Is Very Easy"
s1=str.split()
s2=s1[::-1]
output=" ".join(s2)
print(output)
# Q5) Write a Program To REVERSE internal content of each word?
# 1) input: 'Durga Software Solutions'
# 2) output: 'agruD erawtfoS snoituloS'

s="Durga Software Solutions"
s1=s.split()
a=[]
for i in s1:
    a.append(i[::-1])
output=" ".join(a)
print(output)


