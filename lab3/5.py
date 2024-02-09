class Bank:
    def __init__(self, fname, lname, balance):
        self.fname = fname
        self.lname = lname
        self.balance = balance

    def deposit(self, num1):
        if num1 > 0:
            self.balance += num1
            print(self.fname, self.lname, "has", self.balance) 
        else:
            print("A deposit cannot be negative")
    def withdraw(self, num2):
        if num2 <= self.balance:
            self.balance -= num2
            print(self.fname, self.lname, "has", self.balance)
        else:
            print("There is not enough money in the account.")

fname, lname, n = input().split()
n = int(n)
account = Bank(fname, lname, n)

account.deposit(int(input()))
account.withdraw(int(input()))
