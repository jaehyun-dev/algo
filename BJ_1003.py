count = int(input())
num =   []
dp = [0,1,1]

for i in range(3,42):
    dp.append(dp[i-1] + dp[i-2])

for i in range(count):
    num.append(int(input()))

for n in num:
    if n ==0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        print("%s %s"%(dp[n-1],dp[n]))