""" 
Two Sum
Given an integer array nums and an integer target, find indices i and j such that nums[i] + nums[j] == target and i != j.
Assume that every input has exactly one pair of indices i and j that fulfill this condition.
Return the pair of indices with the smaller index first.
Example 1:
Input: nums = [1, 2, 3, 4], target = 5
Output: [0, 3]
Explanation: nums[0] + nums[3] == 5, so we return [0, 3].
Example 2:
Input: nums = [0, -1, 2, -3, -1], target = -2
Output: [1, 4]
"""

class Solution:
    def twoSum(self, nums, target: int):
        for i in range(0, len(nums) - 1):
            for j in range (1, len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
        return []