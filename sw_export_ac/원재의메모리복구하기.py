T = int(input())
for test_case in range(1, T + 1):
    init = input()
    result = 0
    temp = "0"

    for i in range(len(init)):
        if not temp == init[i]:
            temp = init[i]
            result += 1

    print('#' + str(test_case), result)

