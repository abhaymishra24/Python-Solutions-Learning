
# #  problem 9 = Find out the number enter by user that is prime number or not.

# # Solution 9 -


# # first we define the verible as user input

# n= int(input("Enter your Number: "))    

# # then we do iteration of user value and apply logic for check the number is prime or not

# for i in range(2, n):               
#     if(n%i)==0:
#         print("This is not a prime number")
#         break

#     # after check the value we StopIteration by break function

#     # then we give other print statement for prime numbers in else condition

# else: 
#     print("This is prime number")
    
 
n = 5
    
for i in range(1, 11):
    
    if i == 7:
        break
    print(i*n)
    
print("this a table of 2 using for loop.")


for i in range(3, 100, 3):
    if i == 30:
        break
    print(i)
    
print("This is your odd number.")

# table using function and for loop - 

def print_table():
    
    n = int(input("Enter your number: "))
    
    for i in range(1, 11):
        
        print(n*i)
        
print_table()
print("This is your table.")

def print_num():
    
    for i in range(2, 11, 2):
        print(i)
        
print_num()

