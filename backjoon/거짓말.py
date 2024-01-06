from collections import deque

n, m = map(int,input().split())
true_people = list(map(int,input().split()))
true_people.pop(0)
a = [True if i in true_people else False for i in range(n+1)]

partys = list(list(map(int,input().split())) for _ in range(m))
partys.sort(key=lambda x:len(x),reverse=True)

stack = deque()
for i in partys:
    flag = 0
    for j in i[1:]:
        if a[j]:
            stack.appendleft(i)
            flag = 1
            break
    if flag == 0:
        stack.append(i)

print(stack)
# 앞에 우선 진실을 알고 있는 사람이 포함되어 있는 파티들이 먼저 처리되어야함.

count = m

while stack:
    party = stack.popleft()
    print('party =',party[1:])
    for i in party[1:]:
        if a[i]:
            count -= 1
            for j in party[1:]: # 진실을 들은 사람들을 다 체크
                a[j] = True
            print('a =',a)
            temp_stack = deque()
            for k in range(len(stack)): # 진실을 들은사람들 앞으로 당기는 코드
                temp = stack.pop()
                print('temp = ',temp)
                print(stack)
                flag = 0
                for l in temp[1:]: # 파티 사람 중 진실을 들은 사람이 있는지 체크
                    if a[l]:
                        temp_stack.appendleft(temp)
                        # stack.appendleft(temp)
                        flag = 1
                        break
                if flag == 0:
                    temp_stack.append(temp)
                    # stack.append(temp)
            stack = temp_stack
            break
    print(stack, count)

print(count)

#
# print(partys)
# for i in range(m):
#     print(a)
#     print(partys[i][1:])
#     for j in partys[i][1:]:
#         if a[j]:
#             count -= 1
#             for k in partys[i][1:]:
#                 a[k] = True
#             break
