from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount
from Bank import Bank
class Main:
  def main():
    bank = Bank()
    savings_acc = SavingsAccount("SA001","Alice",1000, 2.0)
    bank.add_Account(savings_acc)
    savings_acc.deposit(200)
    savings_acc.withdraw(100)
    savings_acc.apply_interest_rate()

    
    checking_acc = CheckingAccount("CA001","Bob",500, 100)
    bank.add_Account(checking_acc)
    checking_acc.deposit(300)
    try:
        checking_acc.withdraw(1000)
    except ValueError as e:
        print(f"Error: {e}")
    bank.show_all_accounts()
  if __name__ == "__main__":
    main()



