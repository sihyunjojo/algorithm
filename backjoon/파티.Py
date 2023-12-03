def a_find_min_time(doro_list, all_time, checker):
    global a_min_time
    checker[doro_list[0]] = True
    print(checker)
    all_time += doro_list[1]
    if doro_list[0] == x:
        print('all_time', all_time)
        a_min_time = min(all_time, a_min_time)
        return

    for i in doro[doro_list[0]]:
        if not checker[i[0]]:
            a_find_min_time(i, all_time, checker)


def b_find_min_time(doro_list, all_time, checker):
    global b_min_time
    checker[doro_list[0]] = True

    all_time += doro_list[1]
    if doro_list[0] == start_house:
        print('1',doro_list)
        print('start_house',start_house)
        b_min_time = min(all_time, b_min_time)
        return

    for i in doro[doro_list[0]]:
        if not checker[i[0]]:
            a_find_min_time(i, all_time, checker)


n, m, x = map(int, input().split())
doro = list([] for i in range(n + 1))

for _ in range(m):
    start, end, time = map(int, input().split())
    doro[start].append([end, time])

print("doro = ", doro)

time_for_student = []

for start_house in range(1, n + 1):
    if start_house != x:
        a_min_time = float('inf')
        b_min_time = float('inf')
        for doro_element in doro[start_house]:
            a_checker = [False for _ in range(n + 1)]
            a_checker[start_house] = True
            print('element',doro_element)
            a_find_min_time(doro_element, 0, a_checker)
        print()
        for doro_element in doro[x]:
            print('element',doro_element)
            b_checker = [False for _ in range(n + 1)]
            b_checker[x] = True
            b_find_min_time(doro_element, 0, b_checker)
        print(a_min_time)
        print(b_min_time)
    if start_house == x:
        a_min_time = 0
        b_min_time = 0
    time_for_student.append([a_min_time,b_min_time])
    print()
print(time_for_student)
# 3 1 2
# 2 + 4
# 2 1 3
# 1 + 2
# 2 1 3 4
# 1 2 4 = 7
