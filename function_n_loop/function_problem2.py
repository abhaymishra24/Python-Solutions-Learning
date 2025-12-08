
#  write a programm to find out greatest number using function.

def greatnum(a, b, c):                        # here we make function with argument
    if(a>b and a>c):                          # write the logic for great number
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a= 19                          # here we put numbers
b= 10
c= 12

print(greatnum(a, b, c))          # here we print the number

# a programm - 

def fact():
    
    n = (4,5,8,9,2,3)
    k = (min(n))
    if k<10:
        return k*4
     
    
    
fact()

