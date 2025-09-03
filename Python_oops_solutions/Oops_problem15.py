
class Mamber:
    
    def __init__(self, Name, Age, Gmail, Phone, College, Department):
        
        self.Name = Name
        self.Age = Age
        self.Gmail = Gmail
        self.Phone = Phone
        self.College = College
        self.Department = Department

    def store(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Gmail: {self.Gmail}")
        print(f"College: {self.College}")
        print(f"Phone: {self.Phone}")
        print(f"Department: {self.Department}")
        
    def display(self):
        print(f"Name: {self.Name}, Age: {self.Age}, Gmail: {self.Gmail}, Phone: {self.Phone}, College: {self.College}, Department: {self.Department}")
        
    @staticmethod
    def greet():
        print("Hello, Good to see you here")
    

m = Mamber("Abhay", "22", "tehchyu@hhaygamil.com", "786959745", "IIT Delhi", "Computer Science")
m.store()
m.display()
            

# here solve once again - 

class Number:
    
    def get_num():
        
        a = int(input("Enter your number: "))
        b = int(input("Enter your number: "))
        
        c = a*b
        d = a+b
        j = a//b
        
        print(f"Multiply:{c} , ADD is: {d} , Division are: {j}")
        
        

Number.get_num()
