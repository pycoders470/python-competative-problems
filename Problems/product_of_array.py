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
        """
        Calculate product of all elements except the element at each index.

        Pseudocode (Current - O(n²)):
        1. Initialize: prod = []
        2. For each index i in nums:
           a. res = 1
           b. For each index j in nums:
              - if i != j:
                  res = res × nums[j]
           c. append res to prod
        3. Return prod

        Note: This is a brute force O(n²) solution.
        Optimal approach uses prefix/suffix products in O(n) time without division.

        Approach:
        - For each position, multiply all other elements
        - Skip the current index itself

        Time Complexity: O(n²) - nested loops for each element
        Space Complexity: O(1) - excluding output array

        Args:
            nums (List[int]): array of integers

        Returns:
            List[int]: array where result[i] = product of all nums except nums[i]

        Example:
            >>> solution = Solution()
            >>> result = solution.productExceptSelf([1, 3, 5, 7])
            >>> print(result)
            [105, 35, 21, 15]
            # result[0] = 3×5×7 = 105
            # result[1] = 1×5×7 = 35
            # etc.
        """
        prod = []
        
        for i in range(0, len(nums)):
            res = 1
            for j in range(0,len(nums)):
                if i!=j:
                    res=res*nums[j]
            prod.append(res)
        return prod