import itertools
for test_case in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))    #선수들의 실력
    # 실력차이가 k를 초과하는 선수들이 팀에 선발되면 안된다는 것이다.
    # 최대 인원이 되도록

    max_num = []
    max_num1 = []
    arr.sort()

    temp_list = list(i for i in range(len(arr)))

    com_list = list(itertools.combinations(temp_list, 2))

    for i,j in com_list:
        temp1 = arr[i:j+1]
        a1 = max(temp1) - min(temp1)
        if a1 <= k:
            max_num1.append(len(temp1))


    # for i in range(1,len(arr)+1):
    #     temp = arr[:i]
    #     a = max(temp) - min(temp)
    #     if a <= k:
    #         max_num.append(len(temp))
    #     else:
    #         arr.pop(0)
    #         print("pop arr = ",arr)
    #

    if len(max_num1) == 0:
        result = 1
    else:
        result = max(max_num1)

    print(f"#{test_case+1} {result}")
    # print(f"#{test_case+1} {max(max_num)}")
