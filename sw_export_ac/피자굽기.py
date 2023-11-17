from collections import deque

def cook_pizza(h_duck):
    while True:
        cooked_pizza = h_duck.popleft()
        cooked_pizza[1] //= 2

        if cooked_pizza[1] == 0:
            out_pizza = cooked_pizza[0]
            return h_duck, out_pizza

        h_duck.append(cooked_pizza)

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    pizza_cheese = list(map(int, input().split()))
    pizzas = [[i + 1, pizza_cheese[i]] for i in range(len(pizza_cheese))]

    h_duck = deque(pizzas[:n])
    result = []

    for i in range(n, len(pizzas) + n):
        h_duck, out_pizza = cook_pizza(h_duck)
        result.append(out_pizza)
        if i < len(pizzas):
            print(pizzas[i])
            h_duck.append(pizzas[i])

    print(f"#{test_case} {result[-1]}")