def comb_sort(array):
    comb = len(array)
    

    while comb > 1:
        comb = int(comb//1.3)
        swapped = False
        i = 0
        while i + comb < len(array):
            if array[i] > array[i + comb]:
                array[i], array[i + comb] = array[i + comb], array[i]
                swapped = True
            i = i + 1
        if comb == 1 and swapped == False:
            break
    return(array)

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(comb_sort(array))
