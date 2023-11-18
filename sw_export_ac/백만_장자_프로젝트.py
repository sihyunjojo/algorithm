def 돈벌기(moneys):
    most_expensive = moneys[-1]

    전체_구매가 = sum(moneys[:-1])
    매출 = most_expensive * (len(moneys) - 1)
    순이익 = 매출 - 전체_구매가

    print("순이익 = ", 순이익)
    return 순이익


def make_days(day):
    for i in range(len(day)):
        if max(day) == day[i]:
            max_value_index = i
    print("가장 높은 값의 인덱스 = ", max_value_index)

    day = arr[: max_value_index + 1]
    print("날짜들 = ", day)

    other_days = arr[max_value_index + 1:]
    print("나머지 날짜들 = ", other_days)

    return day, other_days



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())  # 자연수
    arr = list(map(int, input().split()))  # 각 날의 매매가를 나타내는 n개의 자연수

    money = 0

    while True:
        if len(arr) == 0:
            break

        sorted_arr = sorted(arr, reverse=True)
        if arr == sorted_arr:
            break

        days, other_days = make_days(arr)
        money += 돈벌기(days)

        arr = other_days

    print(f"#{test_case} {money}")
