"""
Given two strings s and t, determine whether t is an anagram of s. Return true if they are anagrams, and false otherwise.
An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.
Example 1:
Input: s = "god", t = "dog"
Output: true
Example 2:
Input: s = "can", t = "pan"
Output: false

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        for i in s:
            if i in t:
                count+=1 
        if count==len(t):
            return True
        return False