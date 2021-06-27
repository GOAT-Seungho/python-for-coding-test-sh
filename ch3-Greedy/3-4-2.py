# 3-4 : 1이 될 때까지
# N이 100억 이상의 큰 수가 되는 경우

N, K = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (N // K) * K
    result += (N - target)
    N = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break

    # K로 나누기
    result += 1
    N //= K

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (N - 1)
print(result)
