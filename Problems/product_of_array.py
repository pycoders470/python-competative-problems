"""
Product of Array Except Self
Mid
Given an integer array nums, return an array output where output[i] is the product of all elements in nums except for nums[i].
Each product is guaranteed to fit within a 32-bit integer.
Solve this in O(n) time complexity without using the division operation.
Example 1:
Input: nums = [1, 3, 5, 7]
Output: [105, 35, 21, 15]
Example 2:
Input: nums = [2, 4, 6, 8]
Output: [192, 96, 64, 48]
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        
        for i in range(0, len(nums)):
            res = 1
            for j in range(0,len(nums)):
                if i!=j:
                    res=res*nums[j]
            prod.append(res)
        return prod