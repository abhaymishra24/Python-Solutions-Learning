
# # cook your dish here

# def score(sc):
    
#     t = int(input())
    
#     for i in range(t):
        
#         target_score = x - y 
        
#         print(target_score)
        
# x = int(input())
# y = int(input())
# print(score())       
                
def score(x, y, t):
    results = []
    
    for i in range(t):
        target_score = x - y
        results.append(target_score)
    
    return results

t = int(input("Enter the number of test cases: "))
# Input for x and y
x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

# Input for number of test cases
# t = int(input("Enter the number of test cases: "))

# Call the score function and print results
scores = score(x, y, t)
for result in scores:
    print(result)