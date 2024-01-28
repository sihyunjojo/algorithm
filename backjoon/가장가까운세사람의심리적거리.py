for tc in range(int(input())):
    n = int(input())
    arr = list(set(input().split()))

    result = float('inf')
    g_count = 0

    def cal(p1,p2,p3):
        global g_count
        g_count += 1

        count = 0
        for i in range(4):
            if p1[i] != p2[i]:
                count += 1
            if p2[i] != p3[i]:
                count += 1
            if p3[i] != p1[i]:
                count += 1
        return count

    temp = []

    def per(cnt):
        global result
        if len(temp) == 3:
            result = min(cal(temp[0],temp[1],temp[2]),result)
            return

        for i in range(cnt, len(arr)):
            temp.append(arr[i])
            per(i+1)
            temp.pop()

    if len(arr) <= 3:
        print(0)
    else:
        per(0)
        print(result if result != float('inf') else 0)

# 3
# 3
# ENTJ INTP ESFJ
# 4
# ESFP ESFP ESFP ESFP
# 5
# INFP INFP ESTP ESTJ ISTJ