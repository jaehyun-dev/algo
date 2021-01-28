import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
result = 0

def maze(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= n or ty < 0 or ty >= m:
                continue
            if arr[tx][ty] == 0:
                continue
            if arr[tx][ty] == 1:
                arr[tx][ty] = arr[x][y] + 1
                queue.append((tx,ty))

    result = arr[n-1][m-1]
    print(result)


for i in range(n):
    arr.append( list(map(int,sys.stdin.readline().rstrip())))

maze(0,0) 

