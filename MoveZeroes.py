# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(nums):
    # Initialize a pointer for the position to place the next non-zero element
    non_zero_index = 0
    
    # Traverse the array
    for i in range(len(nums)):
        # If the current element is non-zero, place it at the non_zero_index
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    
    # After all non-zero elements are moved, fill the rest of the array with zeros
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
    
    return nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))  