def two_sum(nums, target):
    # Dictionary to store the number and its index
    seen = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # Check if the needed number exists in our map
        if complement in seen:
            return [seen[complement], index]
        
        # Store the current number and its index
        seen[num] = index
        
    return [] # Return empty list if no solution is found

# Example Usage:
nums_list = [2, 7, 11, 15]
target_val = 9
print(f"Indices: {two_sum(nums_list, target_val)}")
