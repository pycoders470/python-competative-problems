from typing import List
from complexity_analyser import complexity_analyzer


class InsertionSort:
    """Insertion sort implementations.

    Provides two small implementations of insertion sort to illustrate the
    algorithmic concept:

    - `InsertionSorting`: a straightforward approach that removes the current
      element and reinserts it in the correct place within the sorted prefix.
    - `OptimisedInsertionSorting`: an in-place shifting approach that moves
      larger elements to the right and writes the current value into the
      correct position (avoids repeated pop/insert operations).

    Both methods sort a list in ascending order and are intended for learning
    purposes. Time complexity for both is O(n^2) in the average and worst case.
    """
    @complexity_analyzer
    def InsertionSorting(self, array: List):
        """
        Simple insertion sort using `pop` and `insert`.

        Pseudocode (actual implementation):
        1. for i = 1 to len(array)-1:
           a. insert_index = i
           b. current_value = array.pop(i)
           c. for j = i-1 down to 0:
              - if array[j] > current_value:
                  insert_index = j
           d. array.insert(insert_index, current_value)
        2. return array

        This method takes the element at index `i`, removes it with `pop`,
        then finds the correct position in the already-sorted prefix and
        reinserts it using `insert`.

        Time Complexity: O(n^2)
        Space Complexity: O(1) (ignoring temporary pop/insert overhead)
        """
        for i in range(1, len(array)):
            insert_index = i
            current_value = array.pop(i)
            for j in range(i - 1, -1, -1):
                if array[j] > current_value:
                    insert_index = j
            array.insert(insert_index, current_value)
        return array
    @complexity_analyzer
    def OptimisedInsertionSorting(self, array):
        """
        Optimized insertion sort using in-place shifts.

        Pseudocode (actual implementation):
        1. for i = 1 to len(array)-1:
           a. insert_index = i
           b. current_value = array[i]
           c. for j = i-1 down to 0:
              - if array[j] > current_value:
                  array[j+1] = array[j]
                  insert_index = j
              - else:
                  break (early exit optimization)
           d. array[insert_index] = current_value
        2. return array

        Rather than popping and reinserting the current element, this method
        shifts larger elements one position to the right and writes the current
        value into the correct slot. Includes early break optimization.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(1, len(array)):
            insert_index = i
            current_value = array[i]
            for j in range(i - 1, -1, -1):
                if array[j] > current_value:
                    array[j + 1] = array[j]
                    insert_index = j
                else:
                    break
            array[insert_index] = current_value
        return array
    
Input = [13,6,89,11,5,4]
object = InsertionSort()
sorted = object.InsertionSorting(Input)
sorted1 = object.OptimisedInsertionSorting(Input)
print("Sorted :- %s" % sorted)
print("Optimised sort :- %s" % sorted1)
