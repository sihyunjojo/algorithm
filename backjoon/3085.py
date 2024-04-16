n = int(input())
arr = [list(input()) for i in range(n)]
max_length = 0

def row():
    global max_length

    for i in range(n):
        for j in range(n):
            candy = arr[i][j]
            length = 0
            for k in range(j,n):
                if candy == arr[i][k]:
                    length += 1
                else:
                    break;
            if max_length < length:
                max_length = length
    
def col():
    global max_length

    for i in range(n):
        for j in range(n):
            candy = arr[i][j]
            length = 0
            for k in range(j,n):
                if candy == arr[k][i]:
                    length += 1
                else:
                    break;
            if max_length < length:
                max_length = length

for i in range(n):
    for j in range(n):
        if j < n-1:
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j] #행으로 바꾸는 코드
            row()
            col()
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j] #원상 복귀
        if i < n-1:
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j] #열로 바꾸는 코드
            row()
            col()
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j] #열로 바꾸는 코드


print(max_length)