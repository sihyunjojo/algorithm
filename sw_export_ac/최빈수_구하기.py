T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input()
    arr = list(map(int,input().split()))

    dict = {}
    for num in arr:
        if num in dict.keys():
            dict[num] += 1
        else:
            dict[num] = 1

    max_value = max(dict.values())

    index_arr = []

    for index, value in dict.items():
        if value == max_value:
            index_arr.append(index)

    result = max(index_arr)

    print(f"#{test_case} {result}")