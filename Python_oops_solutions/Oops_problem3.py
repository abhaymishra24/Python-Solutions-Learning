
# problem number 3= show the train status, fair, and train number.

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
         
    def book(self, fro, to):
            print(f"seat is booked {self.trainNo} from {fro} to {to}")
    
    def status(self):
            print(f"the train is running this time {self.trainNo}")

    def fair(self, fro, to):
            print(f"the train price {fro} to {to} is {randint(555, 2400)}")


t = Train(12600)
t.book("delhi", "Lucknow")
t.status()
t.fair("delhi", "Lucknow")

# here is one question rise if we not use self so is there any issue? lets check 
# we will use only s for entair programm , lets see what happen.

from random import randint

class Train:
    def __init__(s, trainNo):
        s.trainNo = trainNo
         
    def book(s, fro, to):
            print(f"seat is booked {s.trainNo} from {fro} to {to}")
    
    def status(s):
            print(f"the train is running this time {s.trainNo}")

    def fair(self, fro, to):
            print(f"the train price {fro} to {to} is {randint(555, 2400)}")


t = Train(12600)
t.book("delhi", "Lucknow")
t.status()
t.fair("delhi", "Lucknow")

# So here we can see that there is no issue if we use s .   

from random import randint

class Train:
    def __init__(s, trainNo):
        s.trainNo = trainNo
         
    def book(s, fro, to):
            print(f"seat is booked {s.trainNo} from {fro} to {to}")
    
    def status(s):
            print(f"the train is running this time {s.trainNo}")

    def fair(self, fro, to):
            print(f"the train price {fro} to {to} is {randint(555, 2400)}")


t = Train(12600)
t.book("delhi", "Lucknow")
t.status()
t.fair("delhi", "Lucknow")