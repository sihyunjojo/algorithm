# 16진수
# 보물상자 두겅은 시계 방향으로 돌려
# 각변에는 동일 한 개수의 숫자가 있고,
# 시계 방향 순으로 높은 자리 숫장 ㅔ해당하며 하나의 수를 나타냄

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

def make_num(arr):
    list = []

    for j in range(4):
        # 0 ~ 3 , 3 ~ 6
        start = j * (len(arr) // 4)
        end = (j + 1) * (len(arr) // 4)
        list.append((''.join(arr[start:end])))

    for i in range(len(arr)-1):
        temp = [arr[-1]] + arr[:-1]
        for j in range(4):
            # 0 ~ 3 , 3 ~ 6
            start = j * (len(arr) // 4)
            end = (j + 1) * (len(arr) // 4)
            list.append((''.join(arr[start:end])))
            arr = temp

    print("리스트 수 = ",len(list))
    print("list = ", list)
    return set(list)




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,k = map(int,input().split())
    arr = list(input())
    print("arr = ", arr)

    string_nums = make_num(arr)
    print("set개수 = ",len(string_nums))
    print(string_nums)

    nums = list(string_nums)
    nums.sort(reverse=True)
    print(nums)


    if k == len(nums):
        result = nums[-1]
    else:
        result = nums[k - 1]

    print(f"#{test_case} {int(result,16)}")
