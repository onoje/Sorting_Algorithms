def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return(array)

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(bubble_sort(array))
