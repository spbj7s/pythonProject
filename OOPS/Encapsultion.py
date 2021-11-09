#The process of binding /Grouping the data  with the behaviuor with in a unit is called as Encapsulation

class account:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        #Validation and Autherization
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        # Validation and Autherization
        self.__balance=self.__balance+amount
    def getBalance(self):
        # Validation and Autherization
        return  self.__balance
a=account(10000)
print(a.getBalance())
