# 11-5 : 볼링공 고르기

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 교재 답압

# 1부터 10까지이 무게를 담을 수 있는 리스트
array = [0] * 11
for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)


# 다른 방법 (O(n^2))

# result = 0

# for i in range(n-1):
#     for j in range(i+1, n):
#         if data[i] != data[j]:
#             result += 1

# print(result)

# 다른 방법 (조합)
# dup_count = 0

# for i in range(n):
#     if i == n-1:
#         breadata
#     for j in range(i+1, n):
#         if data[i] == data[j]:
#             dup_count += 1

# result = len(list(combinations(data, 2))) - dup_count

# print(result)

