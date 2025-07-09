
# problem number 12 = wirte the following star pattern by for loop

#   *
#  ***
# *****

# Solution 12 -


# first we take input from user

n = int(input("Enter your number: "))

# we use for loops condition for iteration the value given by user

for i in range (1, n+1): 

# first we print the space using n-i pattern

    print(" "* (n-i), end="")             # using (end="") for no new line

# second we print star using 2*i - 1 

    print("*"* (2*i-1), end="")

# third we print all star using again same pattern

    print("")
    