
# Multiple Inheritance (One child having more then one parent (2 or more))

class A:
    def process(self):
        print("Exceuting A")
        
class B(A):
    def process(self):
        print("Exceuting B")
        super().process()
 
class C(B):
    def process(self):
        print("Exceuting C")
        super().process() 
        
class D(C):
    def process(self):
        print("Exceuting D")
        super().process()     

D().process()

class F(D):
    def process(self):
        print("Exceuting F")
        super().process()
        
F().process()  

# For multiple and diamond problem if the common ancestor is also passes as a parameter to the class
# definition - it should be the last among the paramters

class parent1:
    def __init__(self, c):
        self.c = c
        
class parent2:
    def __init__(self, c1):
        self.c1 = c1

class c(parent1, parent2):
    def __init__(self, name, c, c1):
        parent1.__init__(self, c)
        parent2.__init__(self, c1)
        self.name = name
    
    def display(self):
        print(f"{self.name} has the character {self.c}, {self.c1}.")
        
        
c= c('Alpha', 'Abhay', 'Ankita')
c.display() 