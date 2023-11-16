T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    cards = [int(i) for i in list(input().strip())]
    dp = [0 for i in range(10)]
    for card in cards:
        dp[card] += 1

    max_indices = [index for index, value in enumerate(dp) if value == max(dp)]

    print(f"#{test_case} {max_indices[-1]} {max(dp)}")