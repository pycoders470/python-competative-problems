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
|   |── LinkedList/
│   │   ├── SinglyLinkedList.py
│   │   └── DoubleLinkedList.py
│   │   └── CircularLinkedList.py
│   └── complexity_analyser.py
│
└── Problems/
    ├── sums.py
    ├── duplicate_detect.py
    ├── Anagrams.py
    ├── grouping_anagrams.py
    ├── product_of_array.py
    ├── FindSmallestarrayele.py
    ├── ArrayPartition.py
    ├── DigitsInNumber.py
    ├── GCD.py
    ├── IsPrime.py
    ├── Palindrome.py
    └── ReverseInteger.py
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
- Linked List with comprehensive explanantion & implementation

### Day 5
- **New Problem Files with Full Documentation:**
  - **DigitsInNumber.py**: Count digits + Armstrong numbers (narcissistic numbers)
  - **GCD.py**: Three approaches - Brute Force O(n), Euclidean Iterative O(log n), Euclidean Recursive O(log n), plus LCM
  - **IsPrime.py**: Prime checker O(√n), Brute Force prime counting O(n²), Sieve of Eratosthenes O(n log log n)
  - **Palindrome.py**: Check 32-bit integer palindromes with overflow handling
  - **ReverseInteger.py**: Reverse integers with 32-bit constraints
- **All Problem Files Enhanced:**
  - Added comprehensive test cases with expected outputs
  - Formatted demo sections with ✓/✗ status indicators
  - Clear visualization of inputs/outputs/calculations
  - Proper `if __name__ == '__main__':` guards

---

##  Algorithm Guide

### Sorting Algorithms

#### 1. **Bubble Sort**
Compares adjacent elements and swaps them if in wrong order.
```
for i in range(len(array)-1):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
return array
```
⏱️ Time: O(n²) | 💾 Space: O(1)

#### 2. **Selection Sort**
Finds minimum and places it at current position.

**Simple Version (pop/insert):**
```
for i in range(len(array)-1):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    min_value = array.pop(min_index)
    array.insert(i, min_value)
return array
```

**Optimized Version (swap):**
```
for k in range(len(array)-1):
    min_index = k
    for l in range(k+1, len(array)):
        if array[l] < array[min_index]:
            min_index = l
    array[k], array[min_index] = array[min_index], array[k]
return array
```
⏱️ Time: O(n²) | 💾 Space: O(1)

#### 3. **Insertion Sort**
Builds sorted array by inserting elements in correct position.

**Simple Version (pop/insert):**
```
for i in range(1, len(array)):
    insert_index = i
    current_value = array.pop(i)
    for j in range(i-1, -1, -1):
        if array[j] > current_value:
            insert_index = j
    array.insert(insert_index, current_value)
return array
```

**Optimized Version (shift with break):**
```
for i in range(1, len(array)):
    insert_index = i
    current_value = array[i]
    for j in range(i-1, -1, -1):
        if array[j] > current_value:
            array[j+1] = array[j]
            insert_index = j
        else:
            break
    array[insert_index] = current_value
return array
```
⏱️ Time: O(n²) | 💾 Space: O(1)

#### 4. **Quick Sort**
Divides using pivot, conquers recursively.
```
function quickSort(array, start, end):
    if end is None:
        end = len(array) - 1
    if start < end:
        pivot_index = partition(array, start, end)
        quickSort(array, start, pivot_index - 1)
        quickSort(array, pivot_index + 1, end)
    return array

partition(start, end, array):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            swap(array[i], array[j])
    swap(array[i+1], array[end])
    return i + 1
```
⏱️ Time: O(n log n) avg, O(n²) worst | 💾 Space: O(log n)

#### 5. **Merge Sort**
Divides in half, sorts recursively, merges.
```
function mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    leftpart = array[:mid]
    rightpart = array[mid:]
    leftpart = mergeSort(leftpart)
    rightpart = mergeSort(rightpart)
    return merge(leftpart, rightpart)

merge(leftpart, rightpart):
    temp = []
    i = j = 0
    while i < len(leftpart) and j < len(rightpart):
        if leftpart[i] < rightpart[j]:
            temp.append(leftpart[i])
            i += 1
        else:
            temp.append(rightpart[j])
            j += 1
    temp.extend(leftpart[i:])
    temp.extend(rightpart[j:])
    return temp
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

### Linked Lists

Linked lists are linear data structures composed of nodes. Each node contains data and a reference to the next node (and optionally a previous node for doubly linked lists). This repo includes simple node classes and traversal examples.

---

### 📊 Arrays vs Linked Lists Comparison

| Operation | Array | Linked List |
|-----------|-------|-------------|
| **Access/Lookup** | O(1) ⚡ Fast random access via index | O(n) Sequential access required |
| **Insertion** | O(n) May require shifting elements | O(1) Insert if pointer known |
| **Deletion** | O(n) May require shifting elements | O(1) Delete if pointer known |
| **Search** | O(n) Linear scan (O(log n) if sorted with binary search) | O(n) Must traverse from head |
| **Space** | Contiguous memory, fixed size | Dynamic, grows as needed |
| **Memory Overhead** | Minimal, just data | Higher (extra pointers per node) |
| **Cache Performance** | Excellent (data locality) | Poor (scattered memory) |

**When to use Arrays:**
- Need fast random access
- Memory is limited (minimal overhead)
- Data size is known and fixed
- Performance-critical applications

**When to use Linked Lists:**
- Frequent insertions/deletions at known positions
- Size varies significantly
- Don't need random access
- Memory fragmentation concerns

---

#### Singly Linked List (forward traversal)
```
current = head
while current is not None:
    print(current.data)
    current = current.next
```
⏱️ Time: O(n) | 💾 Space: O(n)

#### Doubly Linked List (forward + backward traversal)
```
# forward
current = head
while current is not None:
    print(current.data)
    current = current.next

# backward (start from tail)
current = tail
while current is not None:
    print(current.data)
    current = current.prev
```
⏱️ Time: O(n) | 💾 Space: O(n)

#### Circular Linked List (single loop around)
```
current = head
start = head
print(current.data)
current = current.next
while current != start:
    print(current.data)
    current = current.next
```
⏱️ Time: O(n) per loop | 💾 Space: O(n)

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

#### 7. **Array Partition**
Maximize sum of minimums in pairs. Uses greedy sorting.
```
sort(array)
result = 0
for i in range(0, len(array), 2):
    result += array[i]  # Add only minimum of each pair
return result
```
⏱️ Time: O(n log n) | 💾 Space: O(1)

---

### Number Theory & Digit Problems

#### 1. **Count Digits in Number**
Count how many digits a number has.
```
count = 0
while n != 0:
    digit = n % 10
    n = n // 10
    count += 1
return count
```
⏱️ Time: O(log n) | 💾 Space: O(1)

#### 2. **Armstrong Number (Narcissistic)**
Check if sum of digits raised to power of digit count equals number. Example: 153 = 1³ + 5³ + 3³
```
cube_sum = 0
original = n
while n != 0:
    digit = n % 10
    n = n // 10
    cube_sum += digit ^ 3
return original == cube_sum
```
⏱️ Time: O(log n) | 💾 Space: O(1)

#### 3. **GCD/HCF (Greatest Common Divisor)**

**Brute Force Approach:**
```
gcd = 1
for i in range(1, min(m,n)+1):
    if m % i == 0 AND n % i == 0:
        gcd = i
return gcd
```
⏱️ Time: O(min(m,n)) | 💾 Space: O(1)

**Euclidean Algorithm (Iterative):**
```
while m > 0 AND n > 0:
    if m > n:
        m = m % n
    else:
        n = n % m
return (m == 0) ? n : m
```
⏱️ Time: O(log min(m,n)) | 💾 Space: O(1)

**Euclidean Algorithm (Recursive):**
```
if n == 0:
    return m
return GCD(n, m % n)
```
⏱️ Time: O(log min(m,n)) | 💾 Space: O(log min(m,n))

#### 4. **LCM (Least Common Multiple)**
Using GCD: LCM(a,b) = (a × b) / GCD(a,b)
```
gcd = GCD(a, b)
lcm = (a * b) // gcd
return lcm
```
⏱️ Time: O(log min(a,b)) | 💾 Space: O(log min(a,b))

#### 5. **Prime Checking**

**Trial Division (Optimized):**
```
if n < 2:
    return False
for i in range(2, √n + 1):
    if n % i == 0:
        return False
return True
```
⏱️ Time: O(√n) | 💾 Space: O(1)

**Count Primes - Brute Force:**
```
count = 0
for i in range(2, n):
    is_prime = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
return count
```
⏱️ Time: O(n²) | 💾 Space: O(1)

**Count Primes - Sieve of Eratosthenes (OPTIMAL):**
```
if n < 2:
    return 0
is_prime = [True] * n
is_prime[0] = is_prime[1] = False
for i in range(2, √n + 1):
    if is_prime[i]:
        for j in range(i², n, i):
            is_prime[j] = False
return count of True values
```
⏱️ Time: O(n log log n) | 💾 Space: O(n) - **Most Efficient!**

#### 6. **Palindrome Checker**
Check if integer reads same forwards and backwards.
```
if x < 0:
    return False
original = x
reversed_num = 0
while x > 0:
    reversed_num = reversed_num * 10 + x % 10
    x = x // 10
return reversed_num == original
```
⏱️ Time: O(log x) | 💾 Space: O(1)

#### 7. **Reverse Integer**
Reverse digits of integer with 32-bit overflow handling.
```
sign = 1 if x > 0 else -1
x = abs(x)
reversed_num = 0
while x != 0:
    digit = x % 10
    reversed_num = reversed_num * 10 + digit
    x = x // 10
if reversed_num exceeds 32-bit bounds:
    return 0
return sign * reversed_num
```
⏱️ Time: O(log x) | 💾 Space: O(1)
