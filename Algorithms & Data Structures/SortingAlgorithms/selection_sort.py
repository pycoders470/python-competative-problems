from typing import List
from complexity_analyser import complexity_analyzer

class SelectionSort:

    @complexity_analyzer
    def SimpleSelectionSort(self, array: List):
        """
        Simple Selection Sort Algorithm.
        
        This function sorts an array in ascending order using the selection sort algorithm.
        In each iteration, it finds the smallest element from the unsorted portion of the array
        and places it at the beginning of the unsorted portion.
        
        How it works:
        1. Iterate through each position in the array (except the last)
        2. Find the index of the minimum element in the remaining unsorted portion
        3. Remove the minimum element and insert it at the current position
        4. Repeat until the array is sorted
        
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
        
        This is an optimized version of selection sort that uses element swapping instead of
        removing and inserting elements. This approach eliminates the costly pop and insert
        operations, making it more efficient in practice.
        
        How it works:
        1. Iterate through each position in the array (except the last)
        2. Find the index of the minimum element in the remaining unsorted portion
        3. Swap the current element with the minimum element (if they differ)
        4. Repeat until the array is sorted
        
        Advantages over SimpleSelectionSort:
        - Avoids expensive pop() and insert() operations
        - Reduces unnecessary element shifts
        - Better performance on arrays with larger elements
        
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
