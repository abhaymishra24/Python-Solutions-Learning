
# problem number 13 = wirte the following star pattern by for loop

#  *
#  **
#  ***

# Solution 13 -


# first we take input from user

n = int(input("Enter your number: "))

# we use for loops condition for iteration the value given by user

for i in range (1, n+1): 

# first we print the star print with i times (it is similer to question number 12)

    print("*"* i, end="")

# second we print all star using again same pattern

    print("")