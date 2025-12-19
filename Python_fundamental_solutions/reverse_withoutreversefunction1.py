
# here wtire a program to reverse a string without using inbuilt reverse function - 

def reverse_string(s):
    reversed_s = ""    # Initialize an empty string to store the reversed result
    for char in s:      # Iterate through each character in the input string from start to end
        reversed_s = char + reversed_s   # Prepend the current character to the reversed string
                                         # This places each new character at the beginning of the result
    return reversed_s                    # Return the completely reversed string

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

"""
    Reverse a string without using built-in reverse functions.
    
    This function takes a string as input and returns a new string with 
    all characters in reverse order. It works by iterating through each 
    character in the original string from left to right, and prepending 
    each character to the result string (adding it to the beginning).
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: A new string with characters in reverse order.
    
    Example:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("Python")
        "nohtyP"
    
    Time Complexity:
        O(n²) - Because string concatenation in Python creates a new string
        each time, resulting in quadratic time complexity.
    
    Space Complexity:
        O(n) - Additional space used for the reversed string.
    
    Note:
        While this implementation works correctly, it's inefficient for 
        large strings due to string immutability in Python. Consider using
        s[::-1] or other approaches for better performance.
"""

