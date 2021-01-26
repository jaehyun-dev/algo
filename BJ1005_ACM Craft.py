import sys

T = int(sys.stdin.readline())        #-- 테스트케이스 개수
m_time  = {}            #-- make_time -> n번빌딩 : 짓는데 걸리는 시간
b_path  = {}            #-- building_path -> to : from 
start = 1000
result_arr  = []
result = 0
for i in range(T):      #-- 테스트케이스 수만큼 돌며 실행
    N, K        = sys.stdin.readline().split()
    b_time      = sys.stdin.readline().split()
    for j in range(int(N)):
        m_time[j+1] = int(b_time[j])
    for k in range(int(K)):
        path = input().split()
        from_p = int(path[0])
        to_p    = int(path[1])
        if from_p < start:
            start = from_p
        if from_p in b_path:
            if m_time[to_p] > m_time[b_path[from_p]]:         #-- building_path에 널을떄 더 오래걸리는 path를 넣음
                b_path[from_p] = to_p
            else:
                continue
        else:
            b_path[from_p] = to_p

    print(b_path)
    destiny = int(input())
    if destiny  in b_path.keys():
        while 1:
            result += m_time[start]
            start = b_path[start]
            if start == destiny:
                result += m_time[start]
                break
    else:
        result = m_time[destiny]
    result_arr.append(result)
    
for r in result_arr:
    print(r)


#-- import sys
#-- sys.stdin.readline() sys.stdout.write()를 쓰면 실행속도 줄어듬 
#-- queue python으로  해보기 