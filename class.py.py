class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount ,"is deposited...")
        print("Total amount is : ",  self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount ,"is credit...")
        print("Total amount is : ",  self.get_balance())
        
    def get_balance(self):
        return self.balance
        
acc1 = Account(100000, 98765)
acc1.debit(10000)
acc1.credit(5000)
acc1.credit(98700)