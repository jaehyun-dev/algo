import sys

count = 0
N, K = sys.stdin.readline().rstrip()

while N <= K:
    N %= K
    count += 1

print(count + N )