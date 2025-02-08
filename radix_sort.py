def radix_sort(array):
    max_value = max(array)
    place = 1
    while max_value // place > 0:
        count_array = [0] * 10
        output = [0] * len(array)

        for num in array:
            index = num // place
            count_array[index % 10] += 1

        for i in range(1, 10):
            count_array[i] += count_array[i - 1]

        i = len(array) - 1
        while i >= 0:
            num = array[i]
            index = num // place
            output[count_array[index % 10] - 1] = num
            count_array[index % 10] -= 1
            i -= 1

        for i in range(len(array)):
            array[i] = output[i]

        place *= 10

    return array

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(radix_sort(array))
