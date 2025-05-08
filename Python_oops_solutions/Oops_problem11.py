
def containsDuplicate(self, nums):

        n = len(nums)

        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True

        return False     
    
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Example usage
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 1]

print(contains_duplicate(nums1))  # Output: False
print(contains_duplicate(nums2))  # Output: True