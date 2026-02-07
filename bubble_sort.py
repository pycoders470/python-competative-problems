array = [64, 34, 25, 12, 22, 11, 90, 5]

def sort_array(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
    return array

print('Sorted array:-',sort_array(array))