"""
Find Smallest Array Element

Given an array of integers, find and return the smallest element.

Example:
Input: [7, 12, 9, 4, 11]
Output: 4

Simple problem to find minimum value in a collection.
"""

def FindSmallest(my_array):
    """
    Find the smallest element in an array.

    Pseudocode:
    1. Initialize: min_value = array[0] (first element)
    2. For each element i in array:
       a. if i < min_value:
          - update min_value = i
    3. Return min_value

    Approach:
    - Start with first element as minimum
    - Compare with each subsequent element
    - Update minimum whenever a smaller element is found
    - Return the final minimum value

    Time Complexity: O(n) - iterate through all elements once
    Space Complexity: O(1) - only uses one variable

    Args:
        my_array (List[int]): array of integers

    Returns:
        int: smallest element in the array

    Example:
        >>> result = FindSmallest([7, 12, 9, 4, 11])
        >>> print(result)
        4
    """
    min_value = my_array[0]
    for i in my_array:
        if i < min_value:
            min_value = i
    return min_value


if __name__ == '__main__':
    print("=" * 50)
    print("Find Smallest Array Element")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        ([7, 12, 9, 4, 11], 4),
        ([1, 2, 3, 4, 5], 1),
        ([5, 4, 3, 2, 1], 1),
        ([100], 100),
        ([50, 50, 50], 50),
        ([-5, -10, -1, -20], -20),
        ([0, -5, 10], -5),
        ([999, 1, 500], 1)
    ]
    
    print("\n--- Testing Find Smallest Element ---")
    for arr, expected in test_cases:
        result = FindSmallest(arr)
        status = "✓" if result == expected else "✗"
        print(f"{status} FindSmallest({arr}) = {result} (expected: {expected})")
    
    print("=" * 50)