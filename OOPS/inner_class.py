# # #A class inside a another class is called as inner class
# #
# #
# # class outer:
# #     def __init__(self):
# #         print("outer class object creation....")
# #     class Inner:
# #         def __init__(self):
# #             print("inner class object creation......")
# #         class InnerInner:
# #             def __init__(self):
# #                 print("InnerInner class object creation......")
# #             @staticmethod
# #             def m1():
# #                 print("Nested Innerclass object creation....")
# # # o=outer()
# # # i=o.Inner()
# # # ii=i.InnerInner()
# # # ii.m1()
# # #outer().Inner().InnerInner().m1()
# # outer().Inner().InnerInner.m1()
#
# #Example 2
# class Human:
#     class head:
#         #@staticmethod
#         def talk(self):
#             print("Talking...")
#         class brain:
#             @staticmethod
#             def think():
#                 print("thinking.......")
# Human.head.talk("p")
# Human.head.brain.think()

#Example 3:

class Person:
    def __init__(self,name,dd,mm,yyyy):

        print("person object creation....")
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)
    def info(self):
        print("hello your name is:",self.name)
        self.dob.display()
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print("DOB object Creation.....")
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
                print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
p=Person('smruti',10,12,1993)
p1=Person('tapasweeni',23,11,2012)
p.info()
p1.info()




