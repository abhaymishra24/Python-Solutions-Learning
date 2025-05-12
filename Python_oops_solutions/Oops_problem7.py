

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

# this is a problem from leetcode  of upper solution -

# You are given an array nums consisting of positive integers.

# We call a subarray of an array complete if the following condition is satisfied:

# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.

# A subarray is a contiguous non-empty part of an array.

# Example 1:

# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
# Example 2:

# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 
# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000