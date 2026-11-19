
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


class F(D, B, C):
    def process(self):
        print("Exceuting F")
        super().process()
        
F().process()  
