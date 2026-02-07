array = [7, 12, 9, 11, 3]
def selection_sort(array):
    for i in range(len(array)-1):
        min_index=i
        for j in range(i+1, len(array)):
            if array[j]<array[min_index]:
                min_index = j
        min_value = array.pop(min_index)
        array.insert(i,min_value)
    return array
print(selection_sort(array))