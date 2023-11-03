# Banking program
from datetime import datetime

class Account:
    bank_name = "Python Bank"
    
    def __init__(self, name, account_number, balance, history = []):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.history = history
        
    def balance_check(self):
        print("Your balance is {} in {} in your {} account".format(self.balance, self.bank_name, self.account_type))
        
    def deposit(self, amount):
        self.balance += amount
        # it should add the deposit to the history except if the deposit function is called via the transfer function
        
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            #print("Your new balance is {}".format(self.balance))
            
    def transfer(self, amount, account):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.withdraw(amount)
            account.deposit(amount)
            
    def show_history(self):
        for i in self.history:
            print(i)
            
            
class Personal(Account):
    account_type = "Personal"
    def __init__(self, name, account_number, balance, history = []):
        super().__init__(name, account_number, balance)
        
    def transfer(self, amount, account):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.withdraw(amount)
            account.deposit(amount)
            self.balance -= amount * 0.01
            self.history.append("Transfer of {} to {} on {}".format(amount, account.name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            
    def details(self):
        print("My name is {}".format(self.name))
        print("My idnumber is {}".format(self.account_number))
        print("My balance is {}".format(self.balance))
            
        
class Enterprise(Account):
    account_type = "Enterprise"
    def __init__(self, name, account_number, balance, company_name, transaction_fee = 0.05, history = []):
        super().__init__(name, account_number, balance)
        self.company_name = company_name
        
    def transfer(self, amount, account):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount * 1.05
            account.deposit(amount)
            self.history.append("Transfer of {} to {} on {}".format(amount, account.name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            
    def details(self):
        print("My name is {}".format(self.name))
        print("My idnumber is {}".format(self.account_number))
        print("My company is {}".format(self.company_name))
        print("My balance is {}".format(self.balance))
        
acc1 = Personal("Marco", 112561, 1000)
acc2 = Enterprise("Arnoldi", 112562, 10000, "Marco's Company")

acc1.balance_check()
acc1.deposit(1000)
acc1.balance_check()
acc1.withdraw(500)
acc1.balance_check()

print("_______________________________")

acc2.balance_check()
acc2.deposit(1000)
acc2.balance_check()
acc2.withdraw(500)
acc2.balance_check()
acc2.details()

print("_______________________________")

acc1.transfer(500, acc2)
acc1.balance_check()
acc2.balance_check()
acc1.withdraw(500)
acc1.transfer(100, acc2)

acc1.show_history()