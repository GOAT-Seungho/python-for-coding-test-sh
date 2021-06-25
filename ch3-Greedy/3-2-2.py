# 큰 수의 법칙 다른 풀이

N, M, K = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

first = arr[0]  # 가장 큰 수
second = arr[1]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K+1)) * K
count += M % (K+1)

result = 0
result += (count) * first   # 가장 큰 수 더하기
result += (M - count) * second  # 두 번째로 큰 수 더하기

print(result)
