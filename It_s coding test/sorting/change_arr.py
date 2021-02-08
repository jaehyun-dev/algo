import sys

n, k = map(int, sys.stdin.readline().split())
result = 0

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

#-- a와 b 소팅
a = sorted(a)
b = sorted(b)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

#-- sum(a) 사용 하면됨 
for j in range(n):
    result += a[j]

print(result)
