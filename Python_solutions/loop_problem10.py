
# problem number 10= Write a programme to find the sum of first n natural number using while loops.

# solution 10 -

# solve by while loop - 

# first we take input from user

n = int(input("Enter your number: "))

# we initialize the starting iteration number and sum with zero and one

i = 0
sum = 0

# we use while condition for iteration the value given by user

while(i<=n):

# we add the number with every iteration value on by one and update also
    sum += i
    i += 1

# then print the statement the sum of value

    print(sum)