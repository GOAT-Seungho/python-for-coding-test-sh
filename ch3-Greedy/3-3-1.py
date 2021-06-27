# 3-3 : 숫자 카드 게임
# min() 함수를 이용하는 답안

N, M = map(int, input().split())
result = 0

for i in range(N):
    data = list(map(int, input().split()))
    min_num = min(data)

    result = max(result, min_num)

print(result)
