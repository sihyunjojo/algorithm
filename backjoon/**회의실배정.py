N_MAX = 100, 000
# n logn
n = int(input())
arr = sorted(list(list(map(int, input().split())) for _ in range(n)), key=lambda x: x[1] - x[0])

max_time = max(arr, key=lambda x: x[1])[1]

arr1 = []
temp = [arr[0]]
for i in range(1, n):
    if arr[i - 1][1] - arr[i - 1][0] == arr[i][1] - arr[i][0]:
        temp.append(arr[i])
    else:
        arr1.append(temp)
        temp = [arr[i]]

    if i == n:
        arr1.append(temp)

count = 0
room = [False for _ in range(max_time + 1)]
for a in arr1:  # n
    for i in a:
        if i[1] == i[0]:
            count += 1
            room[i[0]] = True
            continue

        if i[1] - i[0] + 1 == room[i[0]:i[1] + 1].count(False):
            count += 1
            for j in range(i[0], i[1] + 1):
                room[j] = True
            print(i[1], i[0])
            print(room[i[0]:i[1] + 1])
            print(room)
            # 재귀로 풀어야하나...

print(room)
print(count)
# 포함되는 경우는 제외시켜주는게 좋다.
# 겹치는 경우, 경우를 2개로 나눠줘야한다.
# ->
# 따로인 경우, 붙여준다.
# 15
# 1 4
# 7 7
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 7 7
# 7 7
# 7 7
# 2 13
# 12 14
