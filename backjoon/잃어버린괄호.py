s = input().split('-')
answer = 0
first_value = s.pop(0)

x = sum(map(int,(first_value.split('+'))))
if first_value == '-':
    answer -= x
else:
    answer += x

for i in s:
    x = sum(map(int, (i.split('+'))))
    answer -= x

print(answer)
