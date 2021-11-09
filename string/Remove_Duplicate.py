# Write a program to remove duplicate characters from the given
#  input String?
#  Input: AZZZBCDABBCDABBBBCCCCDDDDEEEEEF
#  Output: AZBCDE

s=input("input the string ")

# output=""
# for ch in s:
#     if ch not in output:
#         output=output+ch
# print(output)

# Logic2:
a=[]
for ch in s:
    if ch not in a:
        a.append(ch)
output="".join(a)
print(output)
