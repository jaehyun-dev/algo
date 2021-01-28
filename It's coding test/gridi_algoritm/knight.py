import sys

n = sys.stdin.readline()
x_char = ['a','b','c','d','e','f','g','h']
dx = [1,-1,1,-1,2,2,-2,-2]
dy = [2,2,-2,-2,1,-1,1,-1]
x = n[0]
y = int(n[1])
x = x_char.index(x)
count = 0

for i in range(len(dx)):
    tmp_x = x + dx[i]
    tmp_y = y + dy[i]
    if tmp_x < 1 or tmp_x > 8 or tmp_y < 1 or tmp_y > 8:
        continue
    count += 1

print(count)