from typing import List
from complexity_analyser import complexity_analyzer

def partition(start, end, array):
    """Partition subarray using the Lomuto partition scheme.

    This function selects the last element in the subarray as the pivot,
    reorders the subarray so that all elements less than or equal to the
    pivot come before it, and returns the pivot's final index.

    Args:
        start (int): start index of the subarray to partition
        end (int): end index of the subarray to partition (pivot index)
        array (List): the list being partitioned

    Returns:
        int: the index where the pivot element is finally placed
    """
    pivot_index = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot_index:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[end] = array[end], array[i+1]
    return i+1


class QuickSort:
    
    def QuickSorting(self, array, start=0, end=None):
        """
        QuickSort (recursive) implementation with partitioning.

        Approach (high-level / pseudocode):
        1. If `end` is None, set it to the last index of `array`.
        2. If the subarray has more than one element (start < end):
           a. Partition the subarray around a pivot (here, last element).
           b. Recursively sort the left subarray (start .. pivot-1).
           c. Recursively sort the right subarray (pivot+1 .. end).
        3. Return the array when sorting completes.

        Partition pseudocode (Lomuto scheme):
        - pivot = array[end]
        - i = start - 1
        - for j from start to end-1:
            if array[j] <= pivot:
                i += 1
                swap array[i] and array[j]
        - swap array[i+1] and array[end]
        - return i+1  # pivot final index

        Complexity notes:
        - Average time: O(n log n)
        - Worst time: O(n^2) (degenerate partitions)
        - Space: O(log n) average recursion depth (O(n) worst-case)

        Args:
            array (List): list of comparable elements to sort
            start (int): start index of subarray to sort
            end (int): end index of subarray to sort

        Returns:
            List: the same list sorted in-place (ascending)
        """
        if end is None:
            end = len(array) - 1
        if start < end:
            pivot_index = partition(start, end, array)
            self.QuickSorting(array, start, pivot_index - 1)
            self.QuickSorting(array, pivot_index + 1, end)
        return array

Input = [64, 34, 25, 12, 22, 11, 90, 5]
object = QuickSort()
sorted = object.QuickSorting(Input)
print("Quick sorted :-", sorted)
        

    