
# Code for python - 

def my_decorator (func):
    def wrapper():
        print("before the function")
        func()
        print("after the function")
    return wrapper

@my_decorator 
def greet():
    print("hello")
greet() 

# code again decorator


def my_decorator (func):
    def wrapper():
        print("before the function")
        func()
    return wrapper


def greet():
    print("hello")
new_greet = my_decorator(greet)
new_greet()

# code decorator

def make_loud(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

@make_loud
def greeting(name):
    return "hello" + name

print(greeting("anu"))

# code decorator

def twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@twice
def say_hii():
    print("hiii!")
say_hii()

# Code decorator

def twice(func):
    def wrapper():
        for _ in range(50):
            func()
         
    return wrapper

@twice
def say_hii():
    print("hiii!")
say_hii()

# code my decorator 

def announce(func):
    def wrapper():
        print("Welcome my world")
        func()
    return wrapper

@announce
def course():
    print("python course")
course()

# code my decorator

def login_req(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func()
        print("please log in first")
    return wrapper

@login_req
def view_account():
    print("Account details")
view_account(False)
view_account(True)

# code of decorator 

def check_number(func):
    def wrapper(num):
        if num > 0:
            print(num, "is a Positive number")
        elif num < 0:
            print(num, "is a Negative number")
        else:
            print(num, "is Zero")
        return func(num)
    return wrapper

@check_number
def number(num):
    return num

# Calling the function
number(10)
number(-5)
number(0)
    