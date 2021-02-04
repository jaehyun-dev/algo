import random
import time

starttime = time.time()
arr = [0] * 1000000
for i in range(1000000):
    arr.append(random.randint(0,1000000))

#print(sorted(arr))

arr = sorted(arr)
print("using time ==> %s"%(time.time() - starttime))