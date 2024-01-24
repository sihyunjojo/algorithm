T = int(input())
for test_case in range(1, T + 1):

    food_count, limit_cal = map(int, input().split())
    menus = list(list(map(int, input().split())) for _ in range(food_count))
    menus = sorted(menus, key=lambda x:x[1])

    result = 0

    def make(count, scores, cals):
        global result

        if limit_cal < cals:
            return
        if limit_cal >= cals:
            result = max(result, scores)
        # if result < scores:
        #     result = scores
        if count == food_count:
            return

        make(count+1, scores+menus[count][0], cals+menus[count][1])
        make(count+1, scores, cals)

    make(0,0,0)

    print('#'+str(test_case), result)


