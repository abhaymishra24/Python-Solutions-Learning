
# ## here programm of function - 

# class Talk:
#     def number():
#         n = int(input("Enter your number: "))
        
#         b = n*2
    
#         if b == 10:
#           print("It's ten number")
#           print(b)
#         else:
#           print("It's not number")
#           print(b)
        
#     number()
    
#     def talk():
        
#         t = input()
#         print("Thank you for talk")
        
#     talk()
        

# calculate factorial using fucntion - 

def cal_fact():
    
  n = int(input("Enter ur number:"))
  fact = 1
  
  for i in range(1, n+1):
    
    print(fact**1)
    
cal_fact()


def cal_num():
  
  a =  int(input("Enter your a number:"))
  b =  int(input("Enter your b number:"))
  
  print(f"the user number is total add {a+b} and subtraction is {a-b}.")
  
cal_num()

def print_num():
  
  n = int(input())
  
  for i in range(1, n+1):
    
    print(i)
    
print_num()
print("This is your chossen number.")
  
def reverse_num():
  
  n = int(input("Enter your number:"))
  
  for i in range(100, n-1, -1):
    
    print(i)

reverse_num()
print("this is your reverse loop.")    
    

def circle():
  
  n = int(input("Enter your number:"))
  
  area_of_cirecle = (2*(3.14)*(n*n))
  print(area_of_cirecle)
  
  
circle()
print("this is your area of circle.")

def num():
  
  n = int(input("Enter your number: "))
  
  for i in range(n-1):
    
    print(n+n)
    break
    
num()

