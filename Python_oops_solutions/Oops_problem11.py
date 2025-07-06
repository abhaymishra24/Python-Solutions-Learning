
def containsDuplicate(self, nums):

        n = len(nums)

        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True

        return False     
    
# Using set

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Example usage
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 1]

print(contains_duplicate(nums1))  # Output: False
print(contains_duplicate(nums2))  # Output: True


class Number:
    def __init__(self, num):
        self.num = num

    def is_even(self):
        return self.num % 2 == 0

    def is_odd(self):
        return self.num % 2 != 0
    
# Example usage
num1 = Number(10)   
num2 = Number(15)
print(num1.is_even())  # Output: True
print(num2.is_odd())   # Output: True