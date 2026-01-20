array = [10,5,14,77,21,66,3,45]
def selection_sort(array):
    for i in range(0,len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort(array))