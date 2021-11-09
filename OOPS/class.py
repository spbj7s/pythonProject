# class Student:
#     '''This class is developed by smruti to show the details of the student'''
#     def __init__(self):
#         self.name="smruti"
#         self.roll=101
#         self.mark=70
#     def show(self):
#         print("student name is:",self.name)
#         print("student mark is:",self.mark)
#         print("student roll number is:",self.roll)
# s= Student()
# print(Student.__doc__)
# print(s.mark)
# print(s.name)
# print(s.roll)
# s.show()
#how to dynamically input a name in

class Student:
    def __init__(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark
    def show(self):
        print("student name is:",self.name)
        print("student roll number is:",self.roll)
        print("student mark name is:",self.mark)
s=Student("smruti",101,70)
s1=Student("Tapasweeni",100,80)
s2=Student("bunny",102,50)
print(Student.__doc__)
print(s.name)
print(s.roll)
print(s.mark)
print(s1.name)
print(s1.roll)
print(s1.mark)
s.show()
s1.show()
s2.show()
