
# problem number 15 = wirte the programm to print multiplication using for loops in reverse table.
 
# Solution 15 -

# first we take input from user

n = int(input("Enter your number: "))

# we use for loops condition for iteration the value given by user

for i in range (1, 11):

# we print the table from 1 to n-1 in print statement

    print(f"{n} X {11-i}= {n*(11-i)}")          # f use for adding verible function perfomance in print statement

# why we use 11 - i ?

# the answer is = starting a normel table from 1 to 10 in staright segment but for reverse we will user n-i for itteration 
# of each value 
