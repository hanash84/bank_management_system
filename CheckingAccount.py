from Account import Account
class CheckingAccount(Account):
    def __init__(self,accountnumber,owner,balance,overdraft_limit):
        self.overdraft_limit=overdraft_limit
        super().__init__(accountnumber,owner,balance)
    def withdraw(self,amount):
        if amount>0:
            max_withdraw = self.overdraft_limit + self.get_balance()
            if amount <= max_withdraw:
               self.set_balance(self.get_balance()-amount)
               print(f"withdraw {amount} New balance {self.get_balance()}")
            else:
               raise ValueError('You cannot withdraw more than maxwithdraw')
        else:
          raise ValueError('Withdraw amount cannot be negative!')
    def deposit(self,amount):
        if amount>0:
            self.set_balance(self.get_balance()+amount)
            print(f"deposited {amount} New balance {self.get_balance()}")
        else:
            raise ValueError('deposit amount cannot be negative!')

