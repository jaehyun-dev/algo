arr = [ 5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tmp_arr = arr[1:]

    left    = [ l for l in tmp_arr if l <= pivot]
    right   = [ r for r in tmp_arr if r > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

#print("before sort ====> %s",arr)


#arr = quicksort(arr)

#print("after sort ====> %s",arr)
