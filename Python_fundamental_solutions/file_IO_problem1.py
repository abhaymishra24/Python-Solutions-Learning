
# We will learn append mode in file IO

st = "Hello, guys I am abhay mishra . welcome to my programming learning. Thankyou"

f = open ("file2.txt", "a")

f.write(st)

f.close

# Here we learn with statement in file IO  


with open ("file1.txt") as f:
    print(f.read())
