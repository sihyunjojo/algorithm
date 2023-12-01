import sys

input = sys.stdin.readline


def calculate(count, price, end_color_index):
    global result
    print(count)
    if count == n:
        result = min(price, result)
        return
    if price > result:
        return
    index_arr = [i for i in range(3) if not i == end_color_index]
    print("index_arr = ", index_arr)

    # if arr[count][index_arr[0]] == arr[count][index_arr[1]]:
    calculate(count + 1, price + arr[count][index_arr[0]], index_arr[0])
    calculate(count + 1, price + arr[count][index_arr[1]], index_arr[1])

    # else:
    #     min_price = min(arr[count][index_arr[0]], arr[count][index_arr[1]])
    #     min_price_index = arr[count].index(min_price)
    #     calculate(count + 1, price + min_price, min_price_index)


def min_price_color(color_prices):
    price = min(color_prices)
    color_index = color_prices.index(price)
    return price, color_index


n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

print("arr = ", arr)
result = float('inf')

start_min_price = min(arr[0])
start_min_price_index = []
for i in range(3):
    if arr[0][i] == start_min_price:
        start_min_price_index.append(i)

print("start_min_price = ", start_min_price)
print("start_min_price_index = ", start_min_price_index)

# for i in start_min_price_index:
#     calculate(1, start_min_price, i)

for i in range(3):
    calculate(1,arr[0][i],i)

print(result)
