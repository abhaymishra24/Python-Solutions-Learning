
# write a solution to find out sum of n number using recursive 

def sum(n):          # difine value
    if(n==1):                    # base condition 
        return 1
    
    return sum(n-1) + n                  # write a logic

n = int(input("Enter your number: "))          # user input
print(sum(n))                            # print final result


# second problem - here we solve the pattern of star with the recusion

# ***
# **
# *

def star(n):
    if(n==0):               # write base condition
        return 0
    print("*"* n)            # print star pattern
    star (n-1)

star(5)                  # print the result

