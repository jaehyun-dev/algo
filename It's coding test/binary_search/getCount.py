import sys
import bisect

n, x = map(int, sys.stdin.readline().split())
arr = list( map(int, sys.readline().split()))

def count_by_range( arr, left, right):
    right_idx = bisect.bisect_right(arr, right)
    left_idx = bisect.bisect_left(arr, left)
    return right_idx - left_idx

count   = count_by_range(arr, x,x)

if count == 0:
    print(-1)
else:
    print(count)