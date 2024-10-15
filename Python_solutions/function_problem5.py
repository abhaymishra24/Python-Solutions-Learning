


# the problem is - write a programm to convert inchs into cms by user given value in function

def inchs_to_cms(inchs):
    return inchs * 2.54                    # the fomula for convert inchs to cms

n = int(input("Enter your number: "))                    # take user input value

print(f"The value of cms is : {inchs_to_cms(n)}")                 # print the final result


# here the second question is - 

# Question is = write multiplication of user given number by function 

def multi(n):
    for i in range(1, 11):               # the logic 
        print(f"{i}X{n}={n*i}")                                      # pattern of multiplication

print(multi(n))                                   # enter final result

# Question number 3 = write a table of 5 till 20 times using function

def table(n):                             # table defination
    for i in range(1, 21):                    # condition number
        print(f"{i}X{n}={n*i}")           # logic to print table

    print(table(5))                         # print final table
    
 