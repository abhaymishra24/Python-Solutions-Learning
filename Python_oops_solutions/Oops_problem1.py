
# Here we learn about Oops concept 

class employee:
    language = "Java, Python"
    Salary = "100000"

    def get(self):
        print(f"Here is information: {self.language}")
        print(f"Here is Salary: {self.Salary}")


emp = employee()
print(emp.language, emp.Salary)

emp.get()

# start method of   @staticmethod

class employee:
    language = "Java, Python"
    Salary = "100000"

    
    def get(self):
        print(f"Here is information: {self.language}")
        print(f"Here is Salary: {self.Salary}")

    @staticmethod
    def greet(self):
        print("Hello, Good to see you here")


emp = employee()
print(emp.language, emp.Salary)

emp.get()
emp.greet()

# end here   @staticmethod


# start init method in oops

# we Learn dunder method here 
# dunder method always call outomaticlay

class employee:
    language = "Java, Python"
    Salary = "100000"


    def __init__(self):              # this called dunder method 
        print("Hello Everyone- ")

    
    def get(self):
        print(f"Here is information: {self.language}")
        print(f"Here is Salary: {self.Salary}")

    @staticmethod
    def greet(self):
        print("Hello, Good to see you here")


emp = employee()
print(emp.language, emp.Salary)

emp.get()
emp.greet()