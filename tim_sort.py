def insertion_sort(array):
    for i in range(len(array)):
        sorted_part = array[i]
        j = i - 1
        while j >= 0 and array[j] > sorted_part:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = sorted_part
        
    return(array)

def merge_sort(array):
    if len(array) > 1:
        middle = len(array)//2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        
        sorted_array = []
        l_i = 0
        r_i = 0
        while l_i < len(left) and r_i < len(right):
            if left[l_i] < right[r_i]:
                sorted_array.append(left[l_i])
                l_i = l_i + 1
            else:
                sorted_array.append(right[r_i])
                r_i = r_i + 1
        sorted_array.extend(left[l_i:])
        sorted_array.extend(right[r_i:])
    
        return sorted_array
    return array

def tim_sort(array):
    min_run = 3
    array_len = len(array)
    
    for start in range(0, array_len, min_run):
        insertion_sort(array[start:start + min_run])

    size = min_run
    while size < array_len:
        for start in range(0, array_len, size * 2):
            middle = min(array_len, start + size)
            end = min(array_len, start + size * 2)
            array[start:end] = merge_sort(array[start:middle] + array[middle:end])
        size *= 2

    return array


array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(tim_sort(array))