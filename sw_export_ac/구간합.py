T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [0] * (n - m + 1)
    for i in range(len(dp)):
        dp[i] = sum(arr[i:i+m])

    print(f"#{test_case} {max(dp) - min(dp)}")




