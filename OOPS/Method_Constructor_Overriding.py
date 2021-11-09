class person:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def display(self):
        print("Name of the person is:",self.name)
        print("Age of the person is:", self.age)
        print("Weight of the person is:", self.weight)
        print("Hieght of the person is:", self.height)
class employee(person):
    def __init__(self,name,age,weight,height,eno,esal):
        super().__init__(name,age,weight,height)
        self.eno=eno
        self.esal=esal
    def display(self):
        super().display()
        print("Employee number is: ",self.eno)
        print("Employee Salary is:",self.esal)
emp=employee("smruti",28,5.8,78,848460,54000)
emp.display()