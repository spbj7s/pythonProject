class person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print("name of the person is: ",self.name)
        print("age of the person is: ",self.age)
        print("height of the person is: ",self.height)
        print("weight of the person is:",self.weight)
class student(person):
    def __init__(self,name,age,height,weight,rollno,marks):
        super().__init__(name,age,height,weight)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print("roll number of the student is :",self.rollno)
        print("mark of the student is: ",self.marks)
s=student("smruti",24,5.8,75,84860,75)
s.display()