# 큰 수의 법칙

N, M, K = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
sum_max = count = 0

for _ in range(M):
    if count == K:
        sum_max += arr[1]
        count = 0
    else:
        sum_max += arr[0]

    count += 1

print(sum_max)
