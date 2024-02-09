class Bank_account:
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
        if num2 < 0:
            print("You cannot withdraw a negative amount of money")
        elif 0 <= num2 <= self.balance:
            self.balance -= num2
            print(self.fname, self.lname, "has", self.balance)
        else:
            print("There is not enough money in the account.")

fname, lname, n = input().split()
n = int(n)
account = Bank_account(fname, lname, n)


while True:
    try:
        s, a = input().split()
        a = int(a)
        if s == "withdraw":
            account.withdraw(a)
        elif s == "deposit":
            account.deposit(a)
    except ValueError:
        break