# 후위표현식의 이해와 스택 자료구조의 활용방법이 중요함.

n = int(input())
s = input()
dict = {}
for i in range(n):
    dict[chr(65+i)] = int(input())
print(dict)

stack = []

for i in s:
    if 'A'<=i<='Z':
        print(dict[i])
        stack.append(dict[i])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i =='+':
            stack.append(str1+str2)
        if i =='-':
            stack.append(str1-str2)
        if i =='*':
            stack.append(str1*str2)
        if i =='/':
            stack.append(str1/str2)

        
print('%.2f'%stack[0])
