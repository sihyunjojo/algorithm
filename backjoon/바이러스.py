computer_amount = int(input())
arr_num = int(input())
arr = list(list(map(int,input().split())) for i in range(arr_num))

temp = [[] for i in range(computer_amount + 1)]
print(arr)

for i in arr:
    temp[i[0]].append(i[1])
    temp[i[1]].append(i[0])

print("temp =",temp)
virus = [1]
result = []

while virus:
    virus_computer = virus.pop()
    result.append(virus_computer)
    for i in temp[virus_computer]:
        print(i)
        if i not in result:
            virus.append(i)
            result.append(i)

print(set(result))

# for i in range(computer_amount + 1):    # 연결된 컴퓨터들 반복
#     for j in temp[i]:
#         if j in virus:
#             virus.append(i)

print(len(set(virus))-1)