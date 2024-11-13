
# In this code we learn function argument.


def goodbye(name, place):
    print("Have a nice day, " + name)        #string concatination
    print(place)

goodbye("Abhay", "from Lucknow")            # function call 
goodbye("Astha", "From Delhi")
goodbye("Sujeet", "From America")


# Here we will learn return concept

def name(city):
    print("Abhay, " + city)
    return 90                      # return statement value


a = name("NewYork")
print(a)                             # print return statment value

# here the also example of return value

def greet(name):
    ge = "hello, " + name          

    return ge                     # return value

a= greet ("harry")
print(a)                          # print return value


# Here we learn default argument

def name(city, country="India"):       # this is defaultu value
    print(f"Welcome to, {city}")
    print(country)

name ("Delhi")                       # if we not put any country name in name fucntion call, so defult value will be India


# Here we understand recursion method 

# we understand rescursion with factorial method

def fact(n):                         # name the function def 
    if(n==1 or n==0):                 # pull condition
        return 1
    return n * fact(n-1)               # write logic for result the code


n = int(input("Enter number: "))              # write code for print the factorial number by user 
print(f"factorial numer is {fact(n)}")        # then call the function for result the user given value