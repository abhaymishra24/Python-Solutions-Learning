
class Account:
    
    def __init__(self, bal, acc):
        
        self.balacne = bal
        self.account_no = acc
        print("Your current balance is:", self.balacne, "Rupees.")
        
    # here we write fuction for debit -
    
    def debit(self, amount):
        
        self.balacne -= amount
        print("Debited from your account:", amount,"Rupees.")
        print("Your current balance is:", self.balacne, "Rupees.")
        
    # here we write function for credit -
    
    def credit(self, amount):
        
        self.balacne += amount
        print("Credited in your account:", amount,"Rupees.")
        print("Your current balance is:", self.balacne, "Rupees.")
        
    # here we write method for finale balance -
    
    def bal(self):
        print("Your current balance is:", self.balacne, "Rupees.")
        

acc1 = Account(20000, 92846624)
acc1.credit(40000)
acc1.debit(15000)
acc1.bal()
    
    
# class Name:
    
#     def __init__ (self, first_name, last_name):
        
#         self.__first_name = first_name
#         self.__last_name = last_name
        
    
# N = Name("Hello", "Hung")
# print(N.__first_name)
# print(N.__last_name)

class Name2:
    
    def __init__(self, name, sir_name):
         
         self.name = name
         self.sir_name = sir_name
         
    def __print(self):
        print("Your name is:", self.name)
        print("Your sir name is:", self.sir_name)
        

ID = Name2("Abhishek", "Diwadi")
print(ID.name)
print(print())
    