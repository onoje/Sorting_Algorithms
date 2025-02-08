def counting_sort(array):
    max_value = max(array)
    count_array = [0] * (max_value + 1)

    for i in array:
        count_array[i] += 1

    sorted_list = []
    for i in range(max_value + 1):
        sorted_list.extend([i] * count_array[i])

    return sorted_list

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(counting_sort(array))