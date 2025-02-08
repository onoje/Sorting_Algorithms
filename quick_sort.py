def quick_sort(array):
    if len(array) > 1:
        pivot = array[-1]

        left = []
        right = []
        for i in range(len(array) - 1):
            if array[i] <= pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        
        sorted_list = quick_sort(left) + [pivot] + quick_sort(right)
        return sorted_list
    return array

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(quick_sort(array))