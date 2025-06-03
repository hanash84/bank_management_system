class Bank:
    def __init__(self):
        self.accounts = []
    def add_Account(self, account):
        self.accounts.append(account)
    def show_all_accounts(self):
        for account in self.accounts:
            account.display_info()