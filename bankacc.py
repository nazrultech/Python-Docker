class Account:

    def __init__(self, bal, acc):
        self.balance= bal
        self.account_no= acc

    def debit(self, amount):
        self.balance -= amount
        self.acc=True
        print("Rs." , amount, "was debited")
        print("Total balance =" , self.get_Balance())

    def credit(self, amount):
        self.balance += amount
        self.acc=True
        print("Rs." , amount, "was credited")
        print("Total balance=" , self.get_Balance())
    
    def get_Balance(self):
        return self.balance

Acc1= Account(10000, 67876677667)
Acc1.debit(1000)
Acc1.credit(3400)
Acc1.credit(156000)