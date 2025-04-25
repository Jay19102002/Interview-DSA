# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is greater than n
    nums[:] = nums[-k:] + nums[:-k]  # Rotate the array in place
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))