import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
result = 0

def check_connect(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if arr[x][y] == 0:
        arr[x][y] = 1       #-- 방문 처리
        check_connect(x-1,y)
        check_connect(x+1,y)
        check_connect(x,y-1)
        check_connect(x,y+1)
        return True
    return False

for i in range(n):
    arr.append( list(map(int,sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(m):
        if check_connect(i,j) == True:
            result += 1

print(result)
