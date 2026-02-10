# Python Competitive Problems & Algorithms

A comprehensive learning repository for competitive programming problems and fundamental algorithms & data structures implemented in Python.

## 📁 Repository Structure

```
python-competative-problems/
├── Algorithms & Data Structures/
│   ├── SortingAlgorithms/
│   │   ├── bubble_sort.py
│   │   ├── selection_sort.py
│   │   ├── InsertionSort.py
│   │   ├── QuickSort.py
│   │   └── MergrSort.py
│   ├── SearchingAlgorithms/
│   │   ├── LinearSearch.py
│   │   └── BinarySearch.py
│   └── complexity_analyser.py
│
└── Problems/
    ├── sums.py
    ├── duplicate_detect.py
    ├── Anagrams.py
    ├── grouping_anagrams.py
    ├── product_of_array.py
    └── FindSmallestarrayele.py
```

##  Daily Progress

### Day 1
- Two Sum - easy
- Duplicate Detection - easy
- Anagram Checking - easy
- Product of Array - medium

### Day 2
- Bubble Sort with Complexity Analyzer
- Selection Sort (Simple & Optimized versions)
- Detailed Docstrings & Complexity Analysis

### Day 3
- Insertion Sort with detailed docstrings (pop/insert & optimized versions)
- Quick Sort implementation with pseudocode and partition explanation
- Merge Sort implementation with bug fix (recursive return capture)
- Comprehensive docstrings with pseudocode for all sorting algorithms
- Complexity analysis decorator applied to all implementations

### Day 4
- Linear Search with detailed docstrings and step-by-step pseudocode
- Binary Search implementation with O(log n) complexity explanation

---

##  Algorithm Guide

### Sorting Algorithms

#### 1. **Bubble Sort**
Compares adjacent elements and swaps them if in wrong order.
```
for i in range(n-1):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            swap(array[j], array[j+1])
```
⏱️ Time: O(n²) | 💾 Space: O(1)

#### 2. **Selection Sort**
Finds minimum and places it at current position.
```
for i in range(n):
    min_index = find_minimum(array[i:])
    swap(array[i], array[min_index])
```
⏱️ Time: O(n²) | 💾 Space: O(1)

#### 3. **Insertion Sort**
Builds sorted array by inserting elements in correct position.
```
for i in range(1, n):
    current = array[i]
    j = i - 1
    while j >= 0 and array[j] > current:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = current
```
⏱️ Time: O(n²) avg, O(n) best | 💾 Space: O(1)

#### 4. **Quick Sort**
Divides using pivot, conquers recursively.
```
function quickSort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quickSort(array, start, pivot_index-1)
        quickSort(array, pivot_index+1, end)
```
⏱️ Time: O(n log n) avg, O(n²) worst | 💾 Space: O(log n)

#### 5. **Merge Sort**
Divides in half, sorts recursively, merges.
```
function mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)
```
⏱️ Time: O(n log n) all cases | 💾 Space: O(n)

---

### Searching Algorithms

#### 1. **Linear Search**
Checks each element sequentially.
```
for i in range(len(array)):
    if array[i] == target:
        return i
return -1
```
⏱️ Time: O(n) | 💾 Space: O(1) | ✅ Works on unsorted arrays

#### 2. **Binary Search**
Halves search space with each iteration (requires sorted array).
```
while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```
⏱️ Time: O(log n) | 💾 Space: O(1) | ⚠️ Requires sorted array

---

### Problem Solutions

#### 1. **Two Sum**
Find two indices that sum to target.
```
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```
⏱️ Time: O(n²) | 💾 Space: O(1)

#### 2. **Duplicate Detection**
Check if array contains duplicates.
```
seen = []
for num in nums:
    if num in seen:
        return True
    seen.append(num)
return False
```
⏱️ Time: O(n) | 💾 Space: O(n)

#### 3. **Anagram Checking**
Verify if two strings are anagrams.
```
if len(s) != len(t):
    return False
for char in s:
    if char in t:
        count += 1
return count == len(t)
```
⏱️ Time: O(n × m) | 💾 Space: O(1)

#### 4. **Group Anagrams**
Group anagrams together from list of strings.
```
groups = {}
for word in strs:
    sorted_word = sort(word)
    if sorted_word in groups:
        groups[sorted_word].append(word)
    else:
        groups[sorted_word] = [word]
return groups.values()
```
⏱️ Time: O(n × k log k) | 💾 Space: O(n)

#### 5. **Product of Array**
Return product of all elements except self.
```
for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product *= nums[j]
    result.append(product)
return result
```
⏱️ Time: O(n²) | 💾 Space: O(1)

#### 6. **Find Smallest Element**
Find minimum element in array.
```
min_value = array[0]
for i in array:
    if i < min_value:
        min_value = i
return min_value
```
⏱️ Time: O(n) | 💾 Space: O(1)
