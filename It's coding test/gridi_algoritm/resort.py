import sys

s = sys.stdin.readline().rstrip()
num = ['0','1','2','3','4','5','6','7','8','9']
result_num = 0
result_str = ''

#-- isalpha() 함수 사용할수도 있음 
for c in s:
    if c in num:
        result_num += int(c)
    else:
        result_str += c

result_str = ''.join(sorted(result_str))        #-- 문자열 오름차순으로 정렬
print(result_str,end ="")
print(result_num)