
# cook your dish here

def score(self):
    
    t = int(input())
    
    for i in range(t):
        
        x , y = map(int, input().split())
        
        target_score = x - y 
        
        print(target_score)