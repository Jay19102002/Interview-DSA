# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

def plusOne(digits):
    # Initialize carry to 1 (since we are adding one)
    carry = 1
    
    # Traverse the digits array from the last digit to the first
    for i in range(len(digits) - 1, -1, -1):
        # Add carry to the current digit
        digits[i] += carry
        
        # If the current digit is less than 10, we can stop
        if digits[i] < 10:
            return digits
        
        # If the current digit is 10, set it to 0 and continue with carry
        digits[i] = 0
    
    # If we finish the loop and still have a carry, we need to add a new digit at the front
    return [1] + digits

digits = [4, 3, 2, 1]
print(plusOne(digits)) 