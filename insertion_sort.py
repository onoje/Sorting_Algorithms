def insertion_sort(array):
    for i in range(len(array)):
        sorted_part = array[i]
        j = i - 1
        while j >= 0 and array[j] > sorted_part:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = sorted_part
        
    return(array)

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(insertion_sort(array))
