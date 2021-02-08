import sys


s = sys.stdin.readline().rstrip()
result = int(s[0])
for n in s[1:]:
    #-- 1인 경우에도 더하기가 더 큰 수가 나옴
    if n == '0' and n == '1':
        result += int(n)
    else:
        result *= int(n)

print(result)