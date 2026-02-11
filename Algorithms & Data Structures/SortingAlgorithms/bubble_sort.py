from typing import List
import random as random
from complexity_analyser import complexity_analyzer 

class BubbleSort:
    """
    Bubble Sort Algorithm Implementation.
    
    Bubble sort is a simple, comparison-based sorting algorithm that repeatedly steps through
    the list, compares adjacent elements, and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    
    The algorithm gets its name because smaller elements "bubble" to the top (beginning) of
    the list with each iteration, while larger elements sink to the bottom (end).
    
    Characteristics:
    - Simple and easy to understand
    - Stable sort (maintains relative order of equal elements)
    - In-place sort (requires minimal extra memory)
    - Not efficient for large datasets
    - Good for educational purposes and nearly sorted data
    """
    
    @complexity_analyzer
    def sort_array(self, array: List):
        """
        Sorts an array in ascending order using the Bubble Sort algorithm.
        
        Pseudocode (actual implementation):
        1. for i = 0 to len(array)-2:
           a. for j = 0 to len(array)-i-2:
              - if array[j] > array[j+1]:
                  swap(array[j], array[j+1])
        2. return array
        
        How it works:
        - Compare each pair of adjacent elements
        - Swap them if the first element is greater than the second
        - After each pass, the largest unsorted element is placed in its correct position
        - Repeat until the entire array is sorted
        
        Time Complexity: O(n²) in all cases
        Space Complexity: O(1) - Sorts in-place with minimal extra space
        
        Args:
            array (List): An unsorted list of comparable elements
            
        Returns:
            List: The sorted array in ascending order
            
        Example:
            >>> sorter = BubbleSort()
            >>> result = sorter.sort_array([64, 34, 25, 12, 22, 11, 90, 5])
            >>> print(result)
            [5, 11, 12, 22, 25, 34, 64, 90]
        """
        for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if array[j]>array[j+1]:
                    array[j],array[j+1] = array[j+1], array[j]
        return array


Input = [64, 34, 25, 12, 22, 11, 90, 5]
Input1 = list(random.sample(range(1,100),50))
object = BubbleSort()
object.sort_array(Input)
object.sort_array(Input1)