
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

