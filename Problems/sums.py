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
        """
        Find two indices whose elements sum to target (Two Sum problem).

        Pseudocode (Brute Force - O(n²)):
        1. For each element at index i:
           a. For each subsequent element at index j:
              - if nums[i] + nums[j] == target and i != j:
                  return [i, j]
        2. Return empty array if no pair found

        Approach:
        - Check all pairs of indices to find matching sum
        - When pair found, return indices with smaller index first

        Time Complexity: O(n²) - nested loops checking all pairs
        Space Complexity: O(1) - only uses a few variables

        Args:
            nums (List[int]): array of integers
            target (int): target sum value

        Returns:
            List[int]: indices [i, j] where nums[i] + nums[j] == target
                      Returns empty list if no pair exists

        Example:
            >>> solution = Solution()
            >>> result = solution.twoSum([1, 2, 3, 4], 5)
            >>> print(result)
            [0, 3]  # nums[0] + nums[3] = 1 + 4 = 5
        """
        for i in range(0, len(nums) - 1):
            for j in range (1, len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
        return []


if __name__ == '__main__':
    print("=" * 50)
    print("Two Sum Problem")
    print("=" * 50)
    
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4], 5, [0, 3]),
        ([0, -1, 2, -3, -1], -2, [1, 4]),
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([1, 1], 2, [0, 1]),
        ([1, 2, 3], 5, [1, 2]),
    ]
    
    print("\n--- Testing Two Sum ---")
    for nums, target, expected in test_cases:
        result = solution.twoSum(nums, target)
        status = "✓" if result == expected else "✗"
        if result:
            sum_val = nums[result[0]] + nums[result[1]]
            print(f"{status} twoSum({nums}, {target}) = {result}")
            print(f"   nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {sum_val}")
        else:
            print(f"{status} twoSum({nums}, {target}) = {result} (No pair found)")
    
    print("=" * 50)