T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump_count = int(input())
    h_arr = list(map(int, input().split()))

    h_arr.sort()

    for i in range(dump_count):
        h_arr[-1] -= 1
        h_arr[0] += 1

        h_arr.sort()
    result = h_arr[-1]-h_arr[0]
    print(f"#{test_case} {result}")

T = 10

for t in range(T):

    N = int(input())
    boxes = list(map(int, input().split()))

    boxes.sort()

    for i in range(N):
        boxes[-1] -= 1
        boxes[0] += 1

        boxes.sort()

    print(f'#{t + 1} {boxes[-1] - boxes[0]}')