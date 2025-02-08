def selection_sort(array):
    for i in range(len(array)): 
        min_value_index = i
        for j in range(i+1, len(array)): 
            if array[j] < array[min_value_index]:
                min_value_index = j
        array[i], array[min_value_index] = array[min_value_index], array[i]

    return (array)

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(selection_sort(array))
