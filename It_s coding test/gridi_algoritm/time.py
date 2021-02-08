import sys

n = int(sys.stdin.readline())
count = 0
for i in range(n+1):
    for m in range(60):
        for s in range(60):
            tmp_time = str(i) + str(m) + str(s)
            if '3' in tmp_time:
                count += 1

print(count)