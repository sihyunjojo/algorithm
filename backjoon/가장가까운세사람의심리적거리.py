for tc in range(int(input())):
    n = int(input())
    arr = list(input().split())

    result = float('inf')
    def cal(p1,p2,p3):
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

        for i in range(cnt, n):
            temp.append(arr[i])
            per(i+1)
            temp.pop()

    if n > 32:
        print(0)
    else:
        per(0)
        print(result)

# 3
# 3
# ENTJ INTP ESFJ
# 4
# ESFP ESFP ESFP ESFP
# 5
# INFP INFP ESTP ESTJ ISTJ