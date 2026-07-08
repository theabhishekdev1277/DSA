#1. Two Sum
#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        seen ={}

        for i, num in enumerate(nums):
            need = target - num 

            if need in seen:
                return [seen[need],i]

            seen[num] = i #this line actually appends the num and their index position in dictionary




































