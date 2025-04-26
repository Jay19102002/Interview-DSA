# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

def containsDuplicate(nums):
    setNums = set()
    for num in nums:
        if num in setNums:
            return True
        setNums.add(num)
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  