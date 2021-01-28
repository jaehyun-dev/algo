import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append( list(map(int,sys.stdin.readline().rstrip())))

print(arr)