import sys

n = sys.stdin.readline()
t = list(sys.stdin.readline().split())
count = 0
t = sorted(t)

for i in range(len(t)):
    if t[i] == 1:
        count += 1
        continue
    else:
        amt = int(t[i])
        tmp = 1
        while True:
            if i+ tmp <=len(t)-1:
                if t[i+tmp] ==  t[i]:
                    amt -= 1
                    if amt == 0:
                        count += 1
                        break
                else:
                    break
            else:
                break

print(count)
            
