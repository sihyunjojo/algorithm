n,m = map(int,input().split())
arr = [""] + list(input() for _ in range(n))
q_arr = list(input() for _ in range(m))

print(arr)
print(q_arr)

for i in q_arr:
    if i.isnumeric():
        print(arr[int(i)])
    else:
        print(arr.index(i))