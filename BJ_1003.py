global num
global zero
global one

num = input()
zero = 0
one = 0

def fibo(n ):
    global zero
    global one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else:
        return fibo(n - 1) + fibo(n-2)

fibo(int(num))
print("%s %s"%(zero,one))