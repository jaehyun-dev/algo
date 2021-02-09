import sys

n = map(int, sys.stdin.readline().split() )
arr = list( map( int, sys.stdin.readline().split()) )

result = 0
jjak    = 0
hol     = 0
for i in range(len(arr)):
    if i % 2 == 0:
        jjak += arr[i] 
    else:
        hol += arr[i]

if jjak > hol :
    result = jjak
else:
    result = hol

print(result)