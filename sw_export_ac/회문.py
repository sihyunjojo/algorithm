def is_palindrome(s):
    return s == s[::-1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(input() for _ in range(n))

    for i in range(n):
        for j in range(m - n + 1):
            if is_palindrome(arr[i][j:j+m]):
                result = arr[i][j:j+m]

    for i in range(m - n + 1):
        for j in range(n):
            if is_palindrome(arr[i][j:j+m]):
                result = arr[i][j:j+m]

    print(result)


