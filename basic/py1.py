a = [1, 2]
# a.remove(2)
print(a)


newList = [i for i in a if a == [1, 2]]
print(newList)
newList = [i for i in a if i == 1]
print(newList)
print()

n = 1
# arr = [0] + [int(input()) for _ in range(n)]
# print(arr)
print("조합")
# nPr 서로 다른 것들 중 몇개를 뽑아서 나열하는것
# nPr : n! / (n-r)!

for i in range(2, 5):
    print(i)

print("델타를 이용한 2차 리스트 탐색")
#델타를 이용한 2차 리스트 탐색
# 가장 끝자리는 조건문 처리를 해줘야한다.
arr = [1, 2, 3], [4, 5, 6]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            # print(arr[testX][testY])

print("전치행렬 (행과 열의 값이 반대인 행렬)")
# 전치행렬 (행과 열의 값이 반대인 행렬)
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        # 모든 좌표에 대해서 적용하면 2번 적용되서 본래 모습으로 돌아옴 주의
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print("부분 집합 알고리즘")
# 부분 집합 알고리즘
# 0000, 0001, 0010, 0011
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
print("이진 검색")
# 이진검색
# 정렬된 리스트에서
# 중앙을 기준으로 중앙값보다 크면 오른쪽 작으면 왼쪽을 검사하는 식으로 반복

# 문자열은 시퀀스 자료형으로 분리되므로, 인덱싱, 슬라이싱 연산 사용가능
a = "abcde"
print(a.replace("a", "c"))
print(a.find("c"))
print(a.find("a"))
print(a[1:3])
print("a=", a)
# 혹시 문자열의 위치에따라서 바꾸고 싶으면 리스트로 바꿔야함.

# 문자열 뒤집기
print("문자열 뒤집기")
original_str = "Hello, World!"
reversed_str = original_str[::-1]

# 패턴 매칭
print("패턴 매칭")
# 무작위 문자열에서 abcd를 찾는다면,
# abcd중에 포함된 걸 찾은 후 -> 인
# b라면 d와 다르므로, 무작위 문자열에서 b를 찾은 위치에서 bcd이므로 2칸뒤에 d가 있는지 확인 (이런식으로 반복)
# +
print(any(char in "abcd" for char in "mkuyo"))
print(any(char in "abcd" for char in "mkayo"))
print(list(char in "abcd" for char in "mkayo"))
print(all(char in "abcd" for char in "abcdwqd"))
print(not all(char in "abcd" for char in "abcdwqd"))

#중요
print("abc" in "abcdef")
print("ac" in "abcdef")

#
# # 가로 세로 회문 찾기
# def is_palindrome(s):
#     return s == s[::-1]
#
# # 가로에서 회문 찾기
# for i in range(N):
#     for j in range(N - M + 1):
#         if is_palindrome(board[i][j:j+M]):
#             print(board[i][j:j+M])
#
# # 세로에서 회문 찾기
# for i in range(N - M + 1):
#     for j in range(N):
#         vertical_str = ''.join(board[k][j] for k in range(i, i+M))
#         if is_palindrome(vertical_str):
#             print(vertical_str)


#파이썬 딕셔너리 넣는 기술
def count_chars(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

count_str1 = {}
count_str2 = {}
#파이썬 딕셔너리 원소 거내기
# 공통으로 나타나는 글자 중 가장 많은 글자의 개수 찾기
max_common_count = 0
for char, count in count_str1.items():
    if char in count_str2:
        max_common_count = max(max_common_count, min(count, count_str2[char]))

# 괄호 검사(딕셔너리 이용, 스택이용)
def is_valid_parentheses(s):
    stack = []

    # 괄호 쌍을 나타내는 딕셔너리
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets.values():
            # 열린 괄호인 경우 스택에 추가
            stack.append(char)
        elif char in brackets.keys():
            # 닫힌 괄호인 경우
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            # 괄호가 아닌 경우는 무시
            pass # 조건문에서 아무것도 하지않음(무시) continue와 다름

    #스택이 비어있으면 모든 괄호가 올바르게 닫혔음을 의미
    return not stack

print("============= 스택 ================")
# 스택관련 코드
# stack[-1] 스택 맨 위의 코드
def remove_repeated_chars(s):
    stack = []

    for char in s:
        # 스택이 비어있지 않고 현재 문자가 스택의 맨 위에 있는 문자와 같으면 반복 문자이므로 스택에서 제거
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # 아니면 스택에 추가
            stack.append(char)

    # 남은 문자열의 길이 반환
    return len(stack)

#팩토리얼 코드

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_dp(n):
    if n == 0 or n == 1:
        return 1

    # DP 테이블 초기화
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]

    return dp[n]

# dp 2*1 그 문제
# memo[n] = count_ways(n - 1, memo) + 2 * count_ways(n - 2, memo)


#DFS 스택으로 구현

def dfs(graph, start, end):
    stack = [start]
    visited = [False] * (len(graph) + 1)

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True

            # 현재 노드와 연결된 모든 노드에 대해
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    return visited[end]



# 노드 수 V, 간선 수 E 입력
def dfs_input():
    V, E = map(int, input().split())

    # 간선 정보를 담은 그래프 생성
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    # 출발 노드 S, 도착 노드 G 입력
    S, G = map(int, input().split())



# DFS 수행 및 결과 출력
# result = dfs(graph, S, G)
# print(1 if result else 0)

# 낙차
def max_gravity_drop(arr):
    gravity = [0] * len(arr[0])
    max_drop = 0

    for col in range(len(arr[0])):
        for row in range(len(arr) - 1, -1, -1):
            if arr[row][col] == 1:
                max_drop = max(max_drop, gravity[col])
                break  # 가장 아래에 있는 상자에 도달했으므로 더 이상 확인하지 않음
            gravity[col] += 1

    return max_drop

# 입력 받기
def input_gravity():
    rows, cols = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(rows)]

# 결과 출력
def output_gravity(boxes):
    result = max_gravity_drop(boxes)
    print(result)

# 후위표기법 계산
# 0. 후위 표기식의 피연산자를 앞부터 하나씩 push함.
# 1. 피연산자를 만나면 스택에 push해야함.
# 2. 연산자를 만나면 필요한 만큼 피연사자를 스택에서 pop하 연산하고, 결과를 Push
# 3. 수식이 끝나면 마지막 스택 pop
print("string 연")
print(eval("6+5*(2-8)/2"))
# print(eval("6528-*2/+"))


#백트래킹
print("백트래킹")

def backtrack(arr, path=[]):
    # 종료 조건: 만들어진 후보가 최종 해결책인 경우
    if len(path) == len(arr):
        print(path)
        return

    # 순열 생성
    for element in arr:
        if element not in path:
            path.append(element)
            backtrack(arr, path)
            path.pop()  # 백트래킹

# 예제 사용
elements = [1, 2, 3]
backtrack(elements)

print("========================")
print("===========Queue==================")
from collections import deque

# 큐 생성
queue = deque([1, 2, 3, 4, 5])
# 원소 추가
queue.append(1)       # 큐의 뒤쪽에 1 추가
queue.appendleft(2)   # 큐의 앞쪽에 2 추가

# print(list(queue))
print(queue)    # deque([])

# 원소 제거
front_element = queue.popleft()  # 큐의 앞쪽에서 원소 제거하고 반환
rear_element = queue.pop()        # 큐의 뒤쪽에서 원소 제거하고 반환
# 큐가 비어있는지 확인
is_empty = not queue

# 큐의 길이 확인
length = len(queue)

# 큐의 모든 원소 출력
print(list(queue))


#우선순위 큐
print("우선순위 큐====")


#BFS
print("BFS=======")
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)  # 노드의 방문 여부를 저장하는 리스트
    queue = deque([start])  # 탐색을 위한 큐에 시작 노드를 넣음
    visited[start] = True  # 시작 노드를 방문했음을 표시

    while queue:
        node = queue.popleft()  # 큐에서 하나의 노드를 꺼냄
        print(node, end=" ")  # 방문한 노드 출력

        # 인접한 노드들 중에서 방문하지 않은 노드를 큐에 추가하고 방문 표시
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# 간단한 그래프를 2차원 리스트로 표현
# 보통 입력값을 이렇게 넣어준 뒤 시작해야함.
graph = [
    [1, 2],
    [0, 3, 4],
    [0, 5],
    [1],
    [1],
    [2]
]

# 시작 노드를 0으로 설정하여 BFS 실행
print("방문한 노드 출력")
bfs(graph, 0)
print()


# 미로 BFS
print("미로 BFS=====")
from collections import deque

def bfs_maze(maze, start, end):
    N = len(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

    queue = deque([(start[0], start[1], 0)])  # 큐에 시작 지점을 넣음
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 저장하는 2차원 리스트
    visited[start[0]][start[1]] = True  # 시작 지점을 방문했음을 표시

    min_distance = float('inf')  # 최소 이동 칸 수
    min_position = (float('inf'), float('inf'))  # 최소 이동 칸 수일 때의 위치

    while queue:
        x, y, distance = queue.popleft()

        # 도착 지점에 도달하면 최소 이동 칸 수와 해당 위치를 갱신
        if (x, y) == end and distance <= min_distance:
            min_distance = distance
            min_position = (x, y)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 미로 범위 내에서 이동 가능하고, 아직 방문하지 않았고, 벽이 아닌 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True  # 방문했음을 표시

    # 도착 지점에 도달할 수 없는 경우
    return min_position

# 최소 이동 칸수가 여러개인 경우, BFS
print("최소 이동 칸수가 여러개인 경우, BFS=====")
def solve_maze():
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    start = None
    end = None

    # 출발지와 도착지 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발지
                start = (i, j)
            elif maze[i][j] == 3:  # 도착지
                end = (i, j)

    result = bfs(maze, start, end)
    print(f"#{test_case} {result[0]} {result[1]}")

# solve_maze()

print()
print("float('inf')는 파이썬에서 무한대(infinity)를 나타내는 값입니다.=====")

# 깊은 복사 얕은 복사
new_list = old_list
new_list = old_list[:] # 깊은 복사
import copy
new_list = copy.deepcopy(old_list) #리스트의 원소지들까 깊은 복사