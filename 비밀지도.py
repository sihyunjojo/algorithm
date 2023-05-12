def two(arr,num):
    result = []
    for i in arr:
        tmp = []
        for j in range(num):
            if i%2 == 1:
                tmp.append(1)
            else:
                tmp.append(0)
            i = i//2
        tmp = tmp[::-1]
        result.append(tmp) 
    return result

def solution(n, arr1, arr2):
    answer = []
    new_arr1 = two(arr1,n)
    new_arr2 = two(arr2,n)
    result = [[' ' for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if new_arr1[i][j] or new_arr2[i][j]:
                result[i][j] = "#"
        answer.append(''.join(result[i]))
        
    return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))