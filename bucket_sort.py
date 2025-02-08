def bucket_sort(array):
    bucket_count = 3
    bucket_size = (max(array) - min(array)) / bucket_count

    buckets = []
    for i in range(bucket_count):
        buckets.append([])

    for number in array:
        bucket_index = int((number - min(array)) // bucket_size)
        if bucket_index == bucket_count:  
            bucket_index -= 1
        buckets[bucket_index].append(number)

    sorted_array = []
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])
        sorted_array.extend(buckets[i])
        
    return(sorted_array)

array = [22, 72, 333, 2, 37, 61, 777, 98, 7]
print(bucket_sort(array))