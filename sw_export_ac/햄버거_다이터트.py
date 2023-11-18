T = int(input())


# food를 함수의 매개변수로 안씀.
# i 라는 반복 횟수를 뜻하는 무언가를 함수에 꼭 넣어줌
# 함수 매개변수에 절대 리스트를 넣어주지 않음.(리스트가 board 같은 경우는 제외)
# 보통 if else로 구현

def knapsack(i,w):
    if k[i][w] != -1:
        return k[i][w]

    if i == 0 or w == 0:
        k[i][w] = 0
        return k[i][w]
    else:
        if w > w[i]:
            return max(knapsack(i-1, w-w[i]) + k[i][w],
                       knapsack(i-1, w))


def cooked(i, score, calo):
    if i == n:
        if calo < L and result <= score:
            return score
        else:
            return 0
    else:
        s, c = foods[i]
        return max(cooked(i+1,score+s,calo+c), cooked(i+1, score,calo))


# 이진검색트리잖아?

def cook(i, score, calo):
    global result
    if i == n:
        if calo < L and result <= score:
            result = score
    else:
        s, c = foods[i]
        cook(i + 1, score + s, calo + c)
        cook(i + 1, score, calo)

    return result


for test_case in range(1, T + 1):
    n, L = map(int, input().split())  # 재료수, 제한칼로리
    foods = []
    for _ in range(n):
        foods.append(list(map(int, input().split())))
    # 같은 재료를 여러 번 사용할 수 없으며, 햄버거의 조합의 제한은 칼로리를 제외하고는 없다.

    result = 0

    print(f"#{test_case} {cooked(0,0,0)}")

