
# here, we solve loops problems 

# this problem solve by for loop

n = int(input("Enter number: "))

for i in range(1, 11):

    print(f"{n} X {i}= {n * i}")

# same problem solve by while loops

n = int(input("Enter your number: "))

i = 1

while(i<11):
    print(f"{n} X {i}= {n*i}")
    i = i+1