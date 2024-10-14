
# the problem is - write a programm to convert inchs into cms by user given value in function

def inchs_to_cms(inchs):
    return inchs * 2.54                    # the fomula for convert inchs to cms

n = int(input("Enter your number: "))                    # take user input value

print(f"The value of cms is : {inchs_to_cms(n)}")                 # print the final result


# here the second question is - 

# Question is = write multiplication of user given number by function 

def multi(n):
    for i in range(1, 11):               # the logic 
        print(f"{i}X{n}={n*i}")            # pattern of multiplication
    
n = int(input("Enter you number: "))           # user number
print(multi(n))                                   # enter final result
 