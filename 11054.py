MAX = 100000000
MAX_N = 1000
print(MAX > MAX_N**2)

n = int(input())
arr = list(map(int,input().split()))

# 앞으로 가다가 제일 큰수가 변경될떄, 그 수가 기존의 큰수보다 작으면 작은걸로 업데이트해야함.

max_num = max(arr)
min_num = min(arr)

tmp = [arr[0]]
result_arr = {}

for i in range(n):
    if min_num < arr[i]:    
        if tmp[-1] < arr[i]:
            tmp.append(arr[i])
        
        elif len(tmp) <= 2:
            if tmp[-1] > arr[i] and min_num < arr[i]:
                tmp.pop()
                tmp.append(arr[i])
        elif len(tmp) > 2:
            if tmp[-1] > arr[i] and min_num < arr[i] and tmp[-2] < arr[i]:
                tmp.pop()   
                tmp.append(arr[i])

    if tmp[-1] > arr[i]  and len(tmp) == 1:
        tmp.pop()
        tmp.append(arr[i])
    

    result_arr[i] = tmp.copy()  # tmp 리스트의 복사본을 딕셔너리에 추가

tmp_b = [arr[-1]]
result_arr_b = {}

for i in range(n-1,-1,-1):
    if min_num < arr[i]:    
        if tmp_b[-1] < arr[i]:
            tmp_b.append(arr[i])
    
        elif len(tmp_b) <= 2:
            if tmp_b[-1] > arr[i] and min_num < arr[i]:
                tmp_b.pop()
                tmp_b.append(arr[i])
        elif len(tmp_b) > 2:
            if tmp_b[-1] > arr[i] and min_num < arr[i] and tmp_b[-2] < arr[i]:
                tmp_b.pop()   
                tmp_b.append(arr[i])
    
    if tmp[-1] > arr[i] and len(tmp_b) == 1:
        print('aaaaaa')
        tmp_b.pop()
        tmp_b.append(arr[i])

    result_arr_b[i] = tmp_b.copy()  # tmp 리스트의 복사본을 딕셔너리에 추가

        
max_len = 0

for i in result_arr:
    max_len = max(max_len, len(result_arr[i]) + len(result_arr_b[i])-1 )

for i in result_arr_b:
    max_len = max(max_len, len(result_arr[i]) + len(result_arr_b[i])-1 )

if len(arr) < 2:
    max_len = len(arr)

print(max_len)
