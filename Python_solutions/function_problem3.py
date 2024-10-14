
# Write a programm to find Fahrenheit into celcius

# first we build function

def f_to_c(f):                        # first define fucntion

    return 5*(f-32)/9                 # write logic and return 

f= int(input("Enter your temp: "))            # take input value from the user 
c = f_to_c(f)                          # call the function

print(f"{round(c, 2)}°C.")                 # print the result



# here we solve a problem where we learn that how to pretend new line in print statement 

# so we can use end="" blank function for avoid line


print("Abhay")
print("is")
print("a ", end="")
print("programmer", end="")           # use of end=" blank space for avoid new line"
