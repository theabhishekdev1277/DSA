#1. Two Sum
#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        got ={}

        for i, num in enumerate(nums):
            need = target - num 

            if need in got:
                return [got[need],i]

            got[num] = i 