def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    pivot_list = []
    right_list = []
    left_list = []
    for i in array:
        if i == pivot:
            pivot_list.append(i)
        elif i > pivot:
            right_list.append(i)
        else:
            left_list.append(i)
    sorted_left = quick_sort(left_list)
    sorted_right = quick_sort(right_list)
    sorted_list = sorted_left + pivot_list + sorted_right
    return sorted_list

lista = [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]
print(quick_sort(lista))