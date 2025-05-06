
# here we write oops code for practice - 

class sellbook:
    
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        
    def display(self):
        print(f"Book Name: {self.name}")
        print(f"Author Name: {self.author}")
        print(f"Price: {self.price}")
        
b = sellbook("Python Programming", "John Doe", 29.99)
b.display() 

class book:
    
    def __init__(self, time, day):
        
        self.time = time
        self.day = day
    
    def mytime(self):
        
        print(f"Read Java book at {self.time} on {self.day}")
        print(f"Read and write some notes on python from {self.time} on anyday.")
        
    def daybyday(self):
        
        print(f"write code and brekdown the code syntax on {self.day}. keep same think for next day other days.")
        print("Ok got it. Happy study and coding practice.")
        
b = book("11:30", "Friday")
b.mytime()
b.daybyday()

