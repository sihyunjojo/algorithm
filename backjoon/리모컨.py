n = input()
m = input()
if m != "0":
    arr = list(map(int, input().split()))
else:
    arr = []

remotecon = [i for i in range(10) if not i in arr]

# 이 리모컨 숫자를 가지고 n과 가장 가까운 값을 만들어야함.
choice = 0

print(remotecon)

for i in range(len(n) - 1, -1, -1):
    # arr = [abs((int(n[i]) * (10 ** i) + choice) - (j * (10 ** i) + choice)) for j in remotecon]
    # arr = [abs(int(n) - (j * (10 ** i) + choice)) for j in remotecon]
    arr = [abs((int(n) - (int(n) % (10 ** i))) - (j * (10 ** i) + choice)) for j in remotecon]
    print(arr)

    for k in range(len(remotecon)):
        if arr[k] == min(arr):
            choice += remotecon[k] * (10 ** i)
            break
    print("choice =", choice)

if n == "100":
    print(0)
elif m == "10":
    print(abs(100 - int(n)))
else:
    print(min(abs(100 - int(n)), len(str(choice)) + abs(choice - int(n))))
