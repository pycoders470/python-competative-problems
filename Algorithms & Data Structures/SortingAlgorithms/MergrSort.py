from typing import List
from complexity_analyser import complexity_analyzer

class MergeSort:
    """
    Merge Sort Implementation (Divide & Conquer).

    Merge sort is a stable, comparison-based sorting algorithm that divides
    the array in half recursively until each subarray has one element, then
    merges them back in sorted order.

    Key characteristics:
    - Stable: maintains relative order of equal elements
    - Divide & Conquer: splits problem into smaller subproblems
    - Guaranteed O(n log n) time complexity
    - Requires O(n) extra space for temporary arrays during merge
    """
    def MergeSorting(self, array: List):
        """
        Recursively sorts an array using Merge Sort.

        Pseudocode:
        1. Base case: if array has 0 or 1 elements, return (already sorted)
        2. Divide: find mid = len(array) // 2
        3. Split: leftpart = array[:mid], rightpart = array[mid:]
        4. Conquer: recursively sort leftpart and rightpart
        5. Combine: merge the two sorted parts and return

        Time Complexity: O(n log n) - all cases (best, average, worst)
        Space Complexity: O(n) - temporary arrays during merge
        Stable: Yes - maintains relative order of equal elements

        Args:
            array (List): unsorted list of comparable elements

        Returns:
            List: sorted list in ascending order
        """
        if len(array) <= 1:
            return array
        mid = len(array)//2

        leftpart = array[:mid]
        rightpart = array[mid:]
        leftpart = self.MergeSorting(leftpart)
        rightpart = self.MergeSorting(rightpart)
        return self.merge(leftpart, rightpart)
        
    def merge(self, leftpart, rightpart):
        """
        Merges two sorted arrays into one sorted array.

        Pseudocode:
        1. Initialize: temp = [], i = 0, j = 0 (pointers for left and right)
        2. Compare: while both pointers are within bounds:
           - if leftpart[i] < rightpart[j]:
               append leftpart[i] and increment i
           - else:
               append rightpart[j] and increment j
        3. Append remaining: add all remaining elements from leftpart and rightpart
        4. Return the merged temp array

        Time Complexity: O(n + m) where n = len(leftpart), m = len(rightpart)
        Space Complexity: O(n + m) - creates new merged array

        Args:
            leftpart (List): first sorted subarray
            rightpart (List): second sorted subarray

        Returns:
            List: merged sorted array combining both inputs
        """
        temp = []
        i = j = 0

        while i<len(leftpart) and j<len(rightpart):
            if leftpart[i] < rightpart[j]:
                temp.append(leftpart[i])
                i+=1
            else:
                temp.append(rightpart[j])
                j+=1
        temp.extend(leftpart[i:])
        temp.extend(rightpart[j:])
        return temp 
    

Input = [64, 34, 25, 12, 22, 11, 90, 5]
object = MergeSort()
sorted = object.MergeSorting(Input)
print("Merge sorted :-", sorted)