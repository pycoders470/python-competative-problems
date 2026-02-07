my_array = [7, 12, 9, 4, 11]
def FindSmallest(my_array):
	min_value = my_array[0]
	for i in my_array:
		if i<min_value:
			min_value = i
	return min_value
print("Smallest element from the array is as:",FindSmallest(my_array))