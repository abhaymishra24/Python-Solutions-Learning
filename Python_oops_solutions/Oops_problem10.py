
# # Program to reverse an integer

# def reverse_integer(n):
#     # Convert the integer to a string, reverse it, and convert it back to an integer
#     reversed_number = int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])
#     return reversed_number

# # Input from the user
# N = int(input("Enter an integer: "))
# print("Reversed Integer:", reverse_integer(N))

# class time:
    
#     def morning(self):
#         n = int(input())
#         if n <= 7:
#             print("get up from bed")
#         elif n > 7:
#             print("get up fast, its too late")
            
#         else:
#             print("get up easily and brush your teeth.")
            
#     def afternoon(self):
        
#         n = int(input())
        
#         if n >= 2 :
#             print("leave laibrary")
            
#         elif n <= 2 :
#             print("don't leave laibrary")
            
#         else:
#             ("study and stay")
            
#     def night(self):
        
#         n = int(input())
        
#         if n >= 8:
#             print("Study at night and revise")
            
#         elif n >= 11:
#             print("watch movie or read book")
            
#         else:
#             print("Sleep or try to sleep")
            
# t = time()
# t.afternoon()
# t.morning()
# t.night()


def number(self, n, m, k):
    
    self.n = n
    self.m = m
    self.k = k
    
    print(f"Money from diferent account:{n+m+k}rupees.")
    print(f"distribute money in other bussiness: {(n+m+k)//10}")   
    
number(1000, 2000, 3000)
number(1000, 2000, 3000)
number(1000, 2000, 3000)    