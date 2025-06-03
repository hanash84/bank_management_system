from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,accountnumber,owner,balance):
        self.__accountnumber=accountnumber
        self.__owner=owner
        self.__balance=balance

    def set_balance(self, balance):
        self.__balance =balance
    def get_balance(self):
        return  self.__balance
    def get_owner(self):
        return self.__owner
    def get_accountnumber(self):
        return self.__accountnumber
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    def display_info(self):
        print(f"AccountNumber:{self.__accountnumber},balance:{self.__balance},owner:{self.__owner}")
