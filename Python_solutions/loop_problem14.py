
 
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