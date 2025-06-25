
class Account:
    
    def __init__(self, bal, acc):
        
        self.balacne = bal
        self.account_no = acc
        
    # here we write fuction for debit -
    
    def debit(self, amount):
        
        self.balacne -= amount
        print("Debited from your account:", amount,"Rupees.")
        
    # here we write function for credit -
    
    def credit(self, amount):
        
        self.balacne += amount
        print("Credited in your account:", amount,"Rupees.")
        
    # here we write method for finale balance -
    
    def bal(self):
        print("Your current balance is:", self.balacne, "Rupees.")
        

acc1 = Account(20000, 92846624)
acc1.credit(40000)
acc1.debit(15000)
acc1.bal()
        