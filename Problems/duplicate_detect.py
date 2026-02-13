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
        """
        Detect if array contains any duplicate elements.

        Pseudocode:
        1. Initialize: temp_array = []
        2. For each element i in nums:
           a. if i NOT in temp_array:
              - append i to temp_array
        3. if len(temp_array) < len(nums):
           - return True (duplicates exist)
        4. Else:
           - return False (no duplicates)

        Approach:
        - Build a collection of unique elements
        - If final collection size < original array size, duplicates exist
        - Uses temporary array to track seen elements

        Time Complexity: O(n) - iterate through array once
        Space Complexity: O(n) - temporary array stores elements

        Args:
            nums (List[int]): array of integers to check

        Returns:
            bool: True if duplicates exist, False otherwise

        Example:
            >>> solution = Solution()
            >>> result = solution.hasDuplicate([1, 1, 2, 3])
            >>> print(result)
            True  # element 1 appears twice
        """
        temp_array = []
        for i in nums:
            if i not in temp_array:
                temp_array.append(i)
        if len(temp_array)<len(nums):
            return True
        return False
    

if __name__ == '__main__':
    print("=" * 50)
    print("Duplicate Detection")
    print("=" * 50)
    
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 1, 2, 3], True),
        ([1, 2, 3, 4], False),
        ([1, 1], True),
        ([1], False),
        ([1, 2, 3, 3, 4], True),
        ([5, 4, 3, 2, 1], False),
        ([1, 1, 1, 1], True),
        ([100, 200, 300], False)
    ]
    
    print("\n--- Testing Duplicate Detection ---")
    for nums, expected in test_cases:
        result = solution.hasDuplicate(nums)
        status = "✓" if result == expected else "✗"
        output = "Duplicates Found" if result else "No Duplicates"
        print(f"{status} hasDuplicate({nums}) = {output}")
    
    print("=" * 50)