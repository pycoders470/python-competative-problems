from typing import List

class BinarySearch:
    """
    Binary Search Algorithm Implementation.

    Binary search is an efficient searching algorithm that works on sorted arrays.
    It eliminates half of the remaining elements with each comparison by dividing
    the search space in half.

    Key characteristics:
    - Works only on sorted arrays
    - Highly efficient for large datasets
    - Divide and conquer approach
    - Much faster than linear search
    - Requires preprocessing (array must be sorted)
    """

    def BinarySearching(self, array: List, target: int):
        """
        Searches for a target element in a sorted array using Binary Search.

        Pseudocode:
        1. Initialize: start = 0, end = len(array) - 1
        2. While start <= end:
           a. Calculate mid = (start + end) // 2
           b. If array[mid] == target:
              return mid (target found)
           c. Else if array[mid] < target:
              start = mid + 1 (search right half)
           d. Else:
              end = mid - 1 (search left half)
        3. Return -1 (target not found)

        Approach:
        - Divide the search space in half with each iteration
        - Compare target with middle element
        - Eliminate half of the remaining elements
        - Continue until target is found or search space is exhausted

        Time Complexity: O(log n)
        - Each iteration eliminates half the elements
        - Maximum iterations = log₂(n)

        Space Complexity: O(1)
        - Only uses a few pointers/variables

        Prerequisites:
        - Array MUST be sorted in ascending order

        Args:
            array (List): sorted list of comparable elements
            target (int): element to search for

        Returns:
            int: index of target if found, -1 if not found

        Example:
            >>> searcher = BinarySearch()
            >>> result = searcher.BinarySearching([1, 2, 3, 4, 5, 6, 7], 5)
            >>> print(result)
            4
        """
        end = len(array) - 1

        while start <= end:
            mid = (start+end)//2

            if target==array[mid]:
                return mid 
            
            if array[mid]<target:
                start = mid + 1
            
            else:
                end = mid - 1
        return -1
Input = [1,2,3,4,5,6,7]
target = 5
object = BinarySearch()
result = object.BinarySearching(array=Input, target=target)

if result != -1:
    print("Target element found at index =", result)
else:
    print('Target element does not exists')

        