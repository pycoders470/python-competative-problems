from typing import List
from complexity_analyser import complexity_analyzer

class SelectionSort:

    @complexity_analyzer
    def SimpleSelectionSort(self, array: List):
        """
        Simple Selection Sort Algorithm.
        
        Pseudocode (actual implementation):
        1. for i = 0 to len(array)-2:
           a. min_index = i
           b. for j = i+1 to len(array)-1:
              - if array[j] < array[min_index]:
                  min_index = j
           c. min_value = array.pop(min_index)
           d. array.insert(i, min_value)
        2. return array
        
        How it works:
        - Iterate through each position and find the minimum element
        - Remove minimum with pop() and reinsert at current position
        - Repeat until the array is sorted
        
        Time Complexity: O(n²) - Due to nested loops
        Space Complexity: O(1) - Sorts in-place (excluding the pop/insert operations)
        
        Args:
            array (List): An unsorted list of comparable elements
            
        Returns:
            List: The sorted array in ascending order
            
        Example:
            >>> sorter = SelectionSort()
            >>> result = sorter.SimpleSelectionSort([7, 12, 9, 11, 3])
            >>> print(result)
            [3, 7, 9, 11, 12]
        """
        for i in range(len(array)-1):
            min_index=i
            for j in range(i+1, len(array)):
                if array[j]<array[min_index]:
                    min_index = j
            min_value = array.pop(min_index)
            array.insert(i,min_value)
        return array

    @complexity_analyzer
    def OptimizedSelectionSort(self, array1: List):
        """
        Optimized Selection Sort Algorithm.
        
        Pseudocode (actual implementation):
        1. for k = 0 to len(array1)-2:
           a. min_index = k
           b. for l = k+1 to len(array1)-1:
              - if array1[l] < array1[min_index]:
                  min_index = l
           c. swap(array1[k], array1[min_index])
        2. return array1
        
        How it works:
        - Find minimum in remaining unsorted portion
        - Swap current position with minimum (no pop/insert overhead)
        - Repeat until array is sorted
        
        Advantages:
        - Avoids expensive pop() and insert() operations
        - In-place swaps are more efficient
        
        Time Complexity: O(n²) - Same as simple selection sort
        Space Complexity: O(1) - Sorts completely in-place with only swaps
        
        Args:
            array1 (List): An unsorted list of comparable elements
            
        Returns:
            List: The sorted array in ascending order
            
        Example:
            >>> sorter = SelectionSort()
            >>> result = sorter.OptimizedSelectionSort([7, 12, 9, 11, 3])
            >>> print(result)
            [3, 7, 9, 11, 12]
        """
        for k in range(len(array1)-1):
            min_index = k
            for l in range(k+1,len(array1)):
                if array1[l]<array1[min_index]:
                    min_index=l
            array1[k], array1[min_index] = array1[min_index],array1[k]
        return array1

Input = [7, 12, 9, 11, 3]
object = SelectionSort()
sort1 = object.SimpleSelectionSort(Input)
sort2 = object.OptimizedSelectionSort(Input)

print("Simple Sort: %s" % sort1)

print("Optimised Sort: %s" % sort2)
