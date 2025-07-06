 
# problem number 14 = wirte the following star pattern by for loop

#  ***
#  * *
#  ***

# Solution 14 -


# first we take input from user

n = int(input("Enter your number: "))

# we use for loops condition for iteration the value given by user

for i in range (1, n+1): 

# first we put condition on star pattern iteration user given number 

    if (i==1 or i==n):
     
# second we print star using n times  
     print("*"* n, end="")
  
# third we print the other condition if uper condition would be not true

    else:
       print("*", end="")
       print(" "* (n-2), end="")
       print("*", end="")
    
# fourth we print all star using again same pattern

    print("")
    
    
def print_star():
    n = int(input("Enter your number: "))
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print("*", end="")
            else:
                if j == 0 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()
        
print_star()


def print_star():
    
    n = int(input("Enter your number:"))    
    for i in range(0, n):
        for j in range(0, n):
            print("*")
        print("*",end="")
        
print_star()

def print_pattern():
    # Number of rows
    rows = 4

    # Outer loop for each row
    for i in range(rows):
        # Inner loop to print 4 stars in each row
        for j in range(4):
            print("*", end="")  # Print star without newline
        print()  # Move to the next line after each row

# Call the function to print the pattern
print_pattern()

# compare this snippet from function_n_loop/loop_problem7.py:

def print_pattern():
    # Ask the user for the number of rows and columns
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Loop through each row
    for i in range(rows):
        # Loop through each column and print stars
        for j in range(cols):
            print("*", end="")  # Stay on the same line
        print()  # Go to the next line after each row

# Call the function
print_pattern()
