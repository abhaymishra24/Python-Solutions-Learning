
#  problem 9 = Find out the number enter by user that is prime number or not.

# Solution 9 -


# first we define the verible as user input

n= int(input("Enter your Number: "))    

# then we do iteration of user value and apply logic for check the number is prime or not

for i in range(2, n):               
    if(n%i)==0:
        print("This is not a prime number")
        break

    # after check the value we StopIteration by break function

    # then we give other print statement for prime numbers in else condition

else: 
    print("This is prime number")


