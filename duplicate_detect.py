"""
Given an integer array nums, determine whether any element appears more than once. Return true if a duplicate exists, and false otherwise.
Example 1:
Input: nums = [1, 1, 2, 3]
Output: true
Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
Constraints:
2 <= nums.length <= 10³
−10⁷ <= nums[i] <= 10⁷
Interview Recommendation:
Aim to create a solution that has O(n) time and space complexity
"""

class Solution:
    def hasDuplicate(self, nums) -> bool:
        temp_array = []
        for i in nums:
            if i not in temp_array:
                temp_array.append(i)
        if len(temp_array)<len(nums):
            return True
        return False
    