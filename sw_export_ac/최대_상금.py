def change(string, a, b):
    string[a], string[b] = string[b], string[a]
    return string


def calculate(string):
    return map(int, string)


import itertools


def all_change(string,combinations):
    n = 0
    while True:
        com_n = 0
        if count == n:
            calculate(string)
        n += 1
        com_n += 1
        all_change(string,combinations[com_n])


def make_combination(string):
    size_list = list(i for i in range(len(string)))
    return list(itertools.combinations(size_list, 2))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    info, count = map(int, input().split())  # 숫자판의 정보, 교환횟수
    info = str(info)
    # 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
    # 맨 앞자리가 이미 제일 큰 숫자로 되어 있으면 안해도 된다. 요곤가?

    now = set([info])
    nxt = set()
    for _ in range(count):
        while now:
            print("now =", now)
            s = now.pop()
            s = list(s)
            # 모든 now 하나씩 바꿔서 넣어줌.
            for i, j in make_combination(info):
                s[i], s[j] = s[j], s[i]
                print("nxt = ",nxt)
                nxt.add(''.join(s))
                s[i], s[j] = s[j], s[i]
            print("count_nxt =",len(nxt))

        print("last_now=",now) # 사실상 set()
        now, nxt = nxt, now

    ans = max(map(int, now))
    print(f'#{test_case} {ans}')

