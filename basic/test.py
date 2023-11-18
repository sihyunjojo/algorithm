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


def bread(i, score, calorie):
    global result
    if i == n:
        if calorie <= l:
            if result < score:
                result = score
    else:
        s, c = lst[i]
        bread(i + 1, score + s, calorie + c)
        bread(i + 1, score, calorie)

    return result


for t in range(int(input())):
    n, l = map(int, input().split())
    lst = []
    result = 0
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    print("#{} {}".format(t + 1, bread(0, 0, 0)))