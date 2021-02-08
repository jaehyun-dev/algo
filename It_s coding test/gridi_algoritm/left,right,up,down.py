import sys

move = ['L', 'R', 'U', 'D']
dx  = [0,0,-1,1]
dy  = [-1,1,0,0]
x = 1
y = 1
n = int(sys.stdin.readline())
plan = list( sys.stdin.readline().rstrip().split())

for p in plan:
    tmp = move.index(p) 
    if x+dx[tmp] < 1 or x+dx[tmp] > n or y+dy[tmp] < 1 or y+dy[tmp] > n:
        continue
    x += dx[tmp] 
    y += dy[tmp] 
print(x,y)