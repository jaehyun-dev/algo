import random
import time

MAX = 100000
def selectsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
starttime = time.time()
arr = [0] * MAX
for i in range(MAX):
    arr.append(random.randint(0,MAX))

arr = selectsort(arr)

print("using time ==> %s"%(time.time() - starttime))