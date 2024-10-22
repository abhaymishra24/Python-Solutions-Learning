
# The question is - make calculater class and find out square, qube, Squareroot.

class calculater:
    def __init__(self, n):
        self.n=n
         
    def square(self):
            print(f"this is square: {self.n*self.n}")
    
    def qube(self):
            print(f"this is qube: {self.n*self.n*self.n}")

    def squareroot(self):
            print(f"this is squareroot: {self.n**1/2}")


cal = calculater(5)
cal.square()
cal.qube()
cal.squareroot()
         