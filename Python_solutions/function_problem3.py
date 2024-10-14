
# Write a programm to find Fahrenheit into celcius

# first we build function

def f_to_c(f):                        # first define fucntion

    return 5*(f-32)/9                 # write logic and return 

f= int(input("Enter your temp: "))            # take input value from the user 
c = f_to_c(f)                          # call the function

print(f"{round(c, 2)}°C.")                 # print the result

