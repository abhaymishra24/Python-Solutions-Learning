
# problem number 11 = find out the factorial number of user given to for loop.

# solution 11 - 

# solve by for loop

# first we take input from user

n = int(input("Enter your number: "))

# we initialize the starting iteration number

product = 1

# we use for loops condition for iteration the value given by user

for i in range (1, n+1):

 # we multipli the each number with every iteration value on by one

    product = product * i
    
# then print the statement the factorial of value

    print(f"the factorial of {n} is {product}")