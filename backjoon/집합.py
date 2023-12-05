import sys

input = sys.stdin.readline


def add(x):
    if not x in s:
        s.append(x)


def remove(x):
    if x in s:
        s.remove(x)


def check(x):
    if x in s:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in s:
        remove(x)
    else:
        add(x)

m = int(input())
s = []

for i in range(m):
    # print('i',i)
    message = input().split()

    if message[0] == "add":
        add(message[1])
    if message[0] == "remove":
        remove(message[1])
    if message[0] == "check":
        check(message[1])
    if message[0] == "toggle":
        toggle(message[1])
    if message[0] == "empty":
        s = []
    if message[0] == "all":
        s = [str(i) for i in range(1, 21)]

# print(s