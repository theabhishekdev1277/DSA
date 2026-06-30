"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS ={}
        countT ={}

        for ch in s:
            if ch in countS:
                countS[ch]+= 1

            else:
                countS[ch]=1

        for ch in t:
            if ch in countT:
                countT[ch]+= 1

            else:
                countT[ch]=1      


        if countS == countT:
            return True

        else:
            return False      


