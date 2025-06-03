from Account import Account
class SavingsAccount(Account):
    def __init__(self,accountnumber,owner,balance,interest_rate):
        self.interest_rate=interest_rate
        super().__init__(accountnumber,owner,balance)
    def apply_interest_rate(self):
        interestamount=self.get_balance()*(self.interest_rate/100)
        self.set_balance(self.get_balance()+interestamount)
        print(f"Interest applied: {interestamount}")
    def deposit(self,amount):
        if amount>0:
            self.set_balance(self.get_balance()+amount)
            print(f"Deposited: {amount}")
        else:
            raise ValueError('Deposit amount cannot be negative!')
    def withdraw(self,amount):
        if amount>0:
            if amount<= self.get_balance():
               self.set_balance(self.get_balance()-amount)
               print(f"Withdrawn: {amount} New balance: {self.get_balance()}")
            else:
               raise ValueError('Withdraw amount cannot be more than your balance!')
        else:
            raise ValueError('Withdraw amount cannot be negative!')


