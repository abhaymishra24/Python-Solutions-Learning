
# Program to reverse an integer

def reverse_integer(n):
    # Convert the integer to a string, reverse it, and convert it back to an integer
    reversed_number = int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])
    return reversed_number

# Input from the user
N = int(input("Enter an integer: "))
print("Reversed Integer:", reverse_integer(N))