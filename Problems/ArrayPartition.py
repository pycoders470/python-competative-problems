"""
Docstring for Problems.ArrayPartition
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
 
"""
class ArrayPartition:
    def arrayPairSum(self, nums):
        """
        Maximize sum of minimums in paired array elements.

        Problem: Given 2n integers, partition into n pairs such that the sum
        of min(ai, bi) for all pairs is maximized.

        Approach (Greedy + Sorting):
        Key insight: To maximize the sum of minimums, we want the smaller
        element in each pair to be as large as possible. Sorting ensures we
        pair adjacent elements where the smaller of each pair is maximized.

        Pseudocode:
        1. Sort the array in ascending order
        2. Initialize result = 0
        3. Iterate through array with step 2 (pairs):
           for i = 0, 2, 4, ... len(nums)-1:
               - add nums[i] to result (the smaller element in each pair)
        4. Return result

        Example walkthrough:
        Input: [6, 2, 6, 5, 1, 2]
        After sort: [1, 2, 2, 5, 6, 6]
        Pairs: (1,2), (2,5), (6,6)
        Sum: 1 + 2 + 6 = 9

        Greedy Strategy:
        - By sorting and picking every other element starting from index 0,
          we ensure each minimum is as large as possible
        - Wasting large numbers as the "max" of a pair maximizes the "min" sum

        Time Complexity: O(n log n) - dominated by sorting
        Space Complexity: O(1) - if sorting in-place, else O(n)

        Args:
            nums (List[int]): list of 2n integers

        Returns:
            int: maximum possible sum of pair minimums
        """
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]
        return res
    
array = [6,2,6,5,1,2]
object = ArrayPartition()
sum = object.arrayPairSum(array)
print("Maximun possible sum is: ", sum)