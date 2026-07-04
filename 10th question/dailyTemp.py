"""
Medium Level Question
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]* len(temperatures)
        stack =[] #this will contain unresolve temperatures 

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prevTemp, prevIndex = stack.pop() #tuple unpacking
                answer[prevIndex] = i - prevIndex

            stack.append((temp,i)) #this will go in unresolved stack we made above

        return answer