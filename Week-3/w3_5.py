import bisect

def twoSum(nums, target):
    
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in nums:
            position2 = bisect.bisect_left(nums, remaining)
            return [i, position2]
   
    return "Not Found"

print(twoSum([2, 7, 11, 15], 9))