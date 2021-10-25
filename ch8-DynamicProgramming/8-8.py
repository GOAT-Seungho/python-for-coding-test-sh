# Ch 8-5 : 효율적인 화폐 구성

n, m = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
array = [10001] * (m+1)
array[0] = 0

for coin in coins:
    for i in range(coin, m+1):
        array[i] = min(array[i], array[i-coin] + 1)


if array[m] == 10001:
    print(-1)
else:
    print(array[m])