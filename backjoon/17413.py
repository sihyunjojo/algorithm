s = input() +' '
flag = 1
tmp = ''

for i in len(s):
    if i == '<':
        print(s[i])
        while i =='>':
            print(i)
    else:
        tmp += i
