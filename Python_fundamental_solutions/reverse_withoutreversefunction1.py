
# here wtire a program to reverse a string without using inbuilt reverse function - 

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s   

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
# print("Reversed string:", reversed_string)

