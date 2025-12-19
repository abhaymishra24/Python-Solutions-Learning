
# write a program to shift number from right to left -

def shift_right_to_left(num, positions):
    # Convert the number to string to manipulate digits
    num_str = str(num)
    length = len(num_str)
    
    # Ensure positions is within the length of the number
    positions = positions % length
    
    # Shift the digits
    shifted_num_str = num_str[positions:] + num_str[:positions]
    
    # Convert back to integer
    shifted_num = int(shifted_num_str)
    
    return shifted_num

# Example usage
number = [1234]    
positions = 4
result = shift_right_to_left(number, positions)
print(f"Original number: {number}")
print(f"Number after shifting {positions} positions from right to left: {result}")


