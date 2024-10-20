
# Here we write first programm for file I/O

# In this programm we learn how to read data from another file

f = open ("file1.txt")
data = f.read()
print(data)
f.close()

# Now we learn how to write data to another file

st = "Hello, guys I am abhay mishra . welcome to my programming learning. Thankyou"

f = open ("file2.txt", "w")

f.write(st)

f.close

