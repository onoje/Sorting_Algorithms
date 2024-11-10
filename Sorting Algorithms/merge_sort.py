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

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(merge_sort(array))