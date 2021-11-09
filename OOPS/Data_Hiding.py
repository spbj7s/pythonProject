class Account:
    def __init__(self,initial_balance):
        self.__balance=initial_balance
    def getBalance(self):
        #validation or authentication
        print("the account balance is:",self.__balance)

a=Account(10000)
a.getBalance()