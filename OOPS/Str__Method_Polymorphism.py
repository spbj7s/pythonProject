#when ever we are tring to print any object refernce internally __str__() method will be called
#by default implementation of this method returns the string in the object refence format
#To provide meaningful string representation for our object we have to override __str__() method in our class


class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def __str__(self):
        return "Name:{} Roll:{} Marks:{}".format(self.name,self.roll,self.marks)
s=student("Smruti",848460,89)
s1=student("Rahul",848462,75)
print(s)
print(s1)