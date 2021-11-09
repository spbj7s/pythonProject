#Instance method is method when we are using instance variable inside a method

class student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hello :",self.name)
        print("Your marks are :",self.marks)
    def grade(self):
        if self.marks >= 60:
            print("you got first grade")
        elif self.marks >= 50:
            print("you got second grade")
        elif self.marks >= 35:
            print("you got third grade")
        else:
            print("you are failed")
n=int(input("enter the number of students :"))
for i in range(n):
    name=input("enter the name :")
    marks=int(input("enter the marks :"))
    s=student(name,marks)
    s.display()
    s.grade()
    print()


