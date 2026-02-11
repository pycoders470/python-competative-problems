from typing import List

class LinearSearch:
    """
    Linear Search Algorithm Implementation.

    Linear search is the simplest searching algorithm. It sequentially checks
    each element of the array against the target value until a match is found
    or the end of the array is reached.

    Key characteristics:
    - Simple and straightforward approach
    - Works on both sorted and unsorted arrays
    - No preprocessing required
    - Not efficient for large datasets
    - Good for small lists or when simplicity is preferred
    """

    def LinearSearching(self, array: List, target: int):
        """
        Searches for a target element in an array using Linear Search.

        Pseudocode:
        1. Initialize: i = 0 (start from first element)
        2. Loop: for each element in array:
           - if current element equals target:
               return the index i
           - increment i
        3. If loop completes without finding target:
           return -1 (not found)

        Approach:
        - Start at the first element (index 0)
        - Check if the current element matches the target
        - If match found, return the index
        - If not found, move to the next element
        - Continue until target is found or array ends
        - Return -1 if target is never found

        Time Complexity: O(n)
        - Best case: O(1) - target at first position
        - Average case: O(n/2) = O(n)
        - Worst case: O(n) - target at last position or not present

        Space Complexity: O(1) - only uses a few variables, no extra space

        Args:
            array (List): list of elements to search through
            target (int): element to search for

        Returns:
            int: index of target if found, -1 if not found

        Example:
            >>> searcher = LinearSearch()
            >>> result = searcher.LinearSearching([3, 7, 2, 9, 5], 9)
            >>> print(result)
            3
        """
        for i in range(len(array)):
            if target == array[i]:
                return i
        return -1
        
Input = [3, 7, 2, 9, 5]
target = 5

object = LinearSearch()
result = object.LinearSearching(array=Input, target=target)
print(result)
if result != -1:
    print("Target element found at index :-", result)
else:
    print('Target element does not exist in array')