
# # print the spam message alert !

# p1= "Buy this one"
# p2= "New product"
# p3= "join now"
# p4= "add some money"
# p5= "Your number has offer"

# message= input("Enter you message:")

# if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message)):

#     print("Danger: This is spam")

# else:
#     print("Safly: This is not spam")


import time

start= time.time()

for i in range(1,100):
    print(i)

print(time.time()- start)