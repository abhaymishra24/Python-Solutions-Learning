

def count_complete_subarrays(arr):
    n = len(arr)
    unique_elements = len(set(arr))
    count = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(arr[j])
            if len(seen) == unique_elements:
                count += 1

    return count

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 1, 3, 2]
    print("Count of complete subarrays:", count_complete_subarrays(arr))
    
# The above code defines a function `count_complete_subarrays` that counts the number of complete subarrays in a given array. A complete subarray is defined as a subarray that contains all unique elements present in the original array. The function uses a nested loop to iterate through all possible subarrays and keeps track of the unique elements seen so far. When the number of unique elements seen matches the total number of unique elements in the original array, it increments the count. Finally, it returns the total count of complete subarrays.
# The example usage demonstrates how to call the function with a sample array and print the result.

def count_complete_subarrays(arr): 
    n = len(arr)
    unique_elements = len(set(arr))
    count = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(arr[j])
            if len(seen) == unique_elements:
                count += 1

    return count

