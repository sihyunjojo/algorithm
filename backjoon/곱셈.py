# 기본적인 반복을 b번을 하면 시간 초과가 나는 문제
# dp로 적당한 규칙이 있나? -> x
# 반복을 줄여서 분할 정복으로 해결해야하는 문제 일거 같다.
# -> 그러나 수학적 공식이 부족하여서 아이디어가 생각이 안남.

# 그래서 공식을 찾아보았습니다.
# 공식을 안다면 쉽게 풀지만, 공식이 머릿속에 바로 떠오르지 않았다면 맞출 수 없는 문제.
# 나머지 분배 법칙
a, b, c = map(int, input().split())


def multi(a, n):
    if n == 1:
        return a % c
    tmp = multi(a, n // 2)
    if n % 2 == 0:
        return (tmp * tmp) % c
    elif n % 2 == 1:
        return (tmp * tmp * a) % c


print(multi(a, b))
