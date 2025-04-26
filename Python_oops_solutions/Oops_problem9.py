
# here we write oops code for practice - 

class book:
    
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        
    def display(self):
        print(f"Book Name: {self.name}")
        print(f"Author Name: {self.author}")
        print(f"Price: {self.price}")
        
b = book("Python Programming", "John Doe", 29.99)
b.display() 