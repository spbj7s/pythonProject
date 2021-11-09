class student:

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n=int(input("enter number of students: "))
list_of_students=[]
for i in range(n):
    s = student()
    name=input("enter student name: ")
    marks=int(input("enter your marks: "))
    s.setName(name)
    s.setMarks(marks)
    list_of_students.append(s)
for s in list_of_students:
    print("Hello ",s.getName())
    print("your mark is ",s.getMarks())




