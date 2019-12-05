class Account(object):

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError("You do not have sufficient funds")

    def __str__(self):
        return f"Account owner is {self.owner} and the available balance is {self.balance}"


# Initiate the class
acct1 = Account('Jose', 100)
# print account
print(acct1)
acct1.deposit(100)
acct1.withdraw(30)
print(f"current account {acct1}")
acct1.withdraw(500000)
