
# write a programm to combine different value in single verible -
# example - [[1,2], [3,4]] = [1,2,3,4]

def combine_values(nested_list):
    combined_list = []
    for sublist in nested_list:
        for item in sublist:
            combined_list.append(item)
    return combined_list

# Example usage
nested_list = [[1, 2], [3, 4]]  
result = combine_values(nested_list)
print("Combined list:", result)  # Output: Combined list: [1, 2, 3, 4]

# Time Complexity: O(n)
# Space Complexity: O(n)


# here code with comments - 

# Define a function that takes a nested list as input
def combine_values(nested_list):
    # Initialize an empty list to store combined values
    combined_list = []
    # Iterate through each sublist in the nested list
    for sublist in nested_list:
        # Iterate through each item in the current sublist
        for item in sublist:
            # Append each item to the combined list
            combined_list.append(item)
    # Return the flattened combined list
    return combined_list

# Create a nested list with two sublists
nested_list = [[1, 2], [3, 4]]
# Call the function and store the result
result = combine_values(nested_list)
# Print the combined list result
print("Combined list:", result)


# solve  this problem again using list comprehension -

def combine_values_list_comprehension(nested_list):
    return [item for sublist in nested_list for item in sublist]

# Example usage
nested_list = [[1, 2], [3, 4]]      
result = combine_values_list_comprehension(nested_list)
print("Combined list using list comprehension:", result)  # Output: Combined list using list comprehension

# time complexity - O(n)
# space complexity - O(n)

