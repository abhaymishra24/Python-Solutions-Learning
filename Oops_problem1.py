
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

