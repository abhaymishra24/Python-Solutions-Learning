
# write a program to shift number from right to left -
# example - 1234 = 4123

def shift_right_to_left(num, positions):
    # Convert the number to string to manipulate digits
    num_str = str(num)
    length = len(num_str)
    
    # Ensure positions is within the length of the number
    positions = positions % length
    
    # Shift the digits
    shifted_num_str = num_str[-positions:] + num_str[:-positions]
    
    # Convert back to integer
    shifted_num = int(shifted_num_str)
    
    return shifted_num

# Example usage
number = 1234   
positions = 2
result = shift_right_to_left(number, positions)
print(f"Original number: {number}")
print(f"Number after shifting {positions} positions from right to left: {result}")

# another method -

def shift_number_right_to_left2():
    n = int(input("Enter number: "))

    last_digit = n % 10
    remaining = n // 10

    digits = len(str(remaining))

    result = last_digit * (10 ** digits) + remaining
    print("Shifted number:", result)

shift_number_right_to_left2()

# here code with comments -

# Define a function to shift the rightmost digit to the left
def shift_number_right_to_left2():
    # Take input from user and convert it to an integer
    n = int(input("Enter number: "))

    # Extract the last digit of the number using modulo operator
    last_digit = n % 10
    # Remove the last digit from the number using integer division
    remaining = n // 10

    # Count the number of digits in the remaining number
    digits = len(str(remaining))

    # Multiply last digit by 10^(number of remaining digits) and add the remaining number
    result = last_digit * (10 ** digits) + remaining
    # Print the shifted number
    print("Shifted number:", result)

# Call the function to execute the code
shift_number_right_to_left2()

