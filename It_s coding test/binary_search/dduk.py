import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start   = 0
end     = max(arr)
result = 0

arr = sorted(arr)
pivot = arr[0]

while start <= end:
    tmp = 0
    mid = (start + end ) //2

    for i in arr:
        if i > mid:
            tmp += i - mid
    if tmp < m:
        end = mid -1
    else:
        result = mid
        start  = mid + 1


print(result)