# ch6-2 : 위에서 아래로

n = int(input())

array = sorted([int(input()) for _ in range(n)], reverse=True)

for a in array:
    print(a, end=' ')