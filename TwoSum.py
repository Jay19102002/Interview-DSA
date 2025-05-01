# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in indices:
            return [indices[complement], i]
        indices[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  