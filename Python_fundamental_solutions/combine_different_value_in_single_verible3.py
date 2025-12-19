
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