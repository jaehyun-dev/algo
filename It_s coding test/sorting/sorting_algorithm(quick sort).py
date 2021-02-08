import random
import time

MAX = 100000
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tmp_arr = arr[1:]

    left    = [ l for l in tmp_arr if l <= pivot]
    right   = [ r for r in tmp_arr if r > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

starttime = time.time()
arr = [0] * MAX
for i in range(MAX):
    arr.append(random.randint(0,MAX))

arr = quicksort(arr)

print("using time ==> %s"%(time.time() - starttime))