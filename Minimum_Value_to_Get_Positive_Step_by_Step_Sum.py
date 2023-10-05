# '''Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 

# Example 1:

# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2
# Example 2:

# Input: nums = [1,2]
# Output: 1
# Explanation: Minimum start value should be positive. 
# Example 3:

# Input: nums = [1,-2,-3]
# Output: 5'''

def helper_function(nums):
    neg_present = 0
    for num in nums:
        if num < neg_present:
            neg_present = num
            return(abs(neg_present) + 1)
    if neg_present == 0:
        return(1)

#print(helper_function([2,3,5,-5,-1])) 

def minStartValue(nums):
    min_start_value = 1
    sum_tracker = 0

    while True:
        for i in range(len(nums)):
            if i == 0:
                sum_tracker = nums[i] + min_start_value 
            elif i != len(nums)-1 and sum_tracker > 0:
                sum_tracker += nums[i]
            elif i == len(nums)-1 and sum_tracker > 0:
                sum_tracker += nums[i]
                if sum_tracker > 0:
                    return min_start_value
        min_start_value += 1
        
            


print(minStartValue([2,3,5,-5,-1])) #1
print(minStartValue([-3, 2, -3, 4, 2]))  # 5
print(minStartValue([1,2])) # 1
print(minStartValue([1, -2, -3]))  # 5
