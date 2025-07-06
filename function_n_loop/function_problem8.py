
def number():
    
    for i in range(5, 50, 5):
        print(i)
        if i == 45:
            print("Its good number which can be divided by 5.")
  
  
number()          
print("Runs loop properly.")

        
# def day_project():
    
#     s = int(input("Enter your hour:"))
    
#     for i in range(1, 6): 

#         if s == 3 or s == 2:
#             print("Project will be completed by 08/07/2025.")
#             break
        
#         elif s == 1:
#             print("It will take time approx by 10/07/2025 to by 11/07/2025.")
#             break
        
#         else:
#             print("Not go project by 12/07/2025.")
        
    
# day_project()


# def get_even_odd():
    
#     n = int(input("Enter number:"))
    
#     for i in range(1, 11, 2):
        
#         num = (n*i)
        
#         if num%2 == 0:
#             print("its is an even number.")
#             break
            
#         else:
#             print("its is an odd number.")
#             break
            
        
# get_even_odd()


def earbuds():
    
    n = int(input("Enter your charging percentage: "))
    
    for i in range(1, 100):
        
        if n < 20:
            print(n+i)
            
        else:
            print(f"Your chareging percentage is {n}.")
            print("Don't need to charge.")
            break
        
earbuds()


def reverse_num():
    # Take input as a space-separated list of numbers
    nums = input("Enter numbers separated by space: ").split()
    nums = [int(x) for x in nums]
    reversed_nums = nums[::-1]
    print("Reversed list:", reversed_nums)
    
reverse_num()