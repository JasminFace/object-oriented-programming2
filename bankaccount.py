# [str(account) for account in BankAccount.accounts]
# [account.__str__() for account in BankAccount.accounts]

# ['Account balance is: $10', 'Account balance is: $920']
# 
# tmp = []
# for account in BankAccount.accounts: 
#     tmp.append(str(account)) 
# tmp

class BankAccount:
    
    interest_rate = float(0.19)
    accounts = []

    def __init__(self, balance = 0):
        self.balance = balance
    
    def __str__(self):
        return f"Account balance is: ${self.balance:.2f}"

    def deposit(self, num):
        self.balance += num
    
    def withdraw(self, num):
        self.balance -= num

    @classmethod
    def create(cls, balance = 0):
        account = BankAccount(balance)
        cls.accounts.append(account)
        return account

    @classmethod
    def total_funds(cls):
        total = 0
        for account in BankAccount.accounts:
            total += account.balance
        return f"Total bank funds: ${total}"

    @classmethod
    def interest_time(cls):
        for account in BankAccount.accounts:
            interest = account.balance * BankAccount.interest_rate
            account.balance += interest

my_account = BankAccount.create()
your_account = BankAccount.create()

print("------STARTING BALANCE------")
print(my_account)
print(your_account)
print("----------DEPOSIT-----------")
my_account.deposit(500)
your_account.deposit(200)
print(my_account)
print(your_account)
print("---------WITHDRAW------------")
my_account.withdraw(80)
your_account.withdraw(57)
print(my_account)
print(your_account)
print("----------INTEREST-----------")
BankAccount.interest_time()
print(my_account)
print(your_account)
print("----------------------------")
print(BankAccount.total_funds())