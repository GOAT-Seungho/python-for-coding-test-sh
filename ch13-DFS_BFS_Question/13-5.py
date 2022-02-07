# Ch13-5 : 연산자 끼워 넣기

'''
ex) 1, 2, 3, 4, 5, 6 / +, +, -, *, /
    5 p 5 / 2! => 60가지 경우의 수

0, 1, 2, 3

1, 2, 3, 4, 5, 6

+, -, *, /
2, 1, 1, 1



'''
from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

# +, -, *, / 의 개수
tok = ['+', '-', '*', '/']
cnt_operations = list(map(int, input().split()))
operations = []
for i in range(len(cnt_operations)):
    for _ in range(cnt_operations[i]):
        operations.append(tok[i])

cases = list(set(permutations(operations, n-1)))

max_result = -1e9
min_result = 1e9

# +, +, -, *, /
for case in cases:
    result = nums[0]
    for i in range(n-1):
        if case[i] == '+':
            result += nums[i+1]
        elif case[i] == '-':
            result -= nums[i+1]
        elif case[i] == '*':
            result *= nums[i+1]
        else:
            if result < 0:
                result = -(abs(result) // nums[i+1])
            else:
                result //= nums[i+1]

    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)



### DFS를 이용하여 푸는 방법 ###
n = int(input())
data = list(map(int, input().split()))
# +, -, *, / 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# DFS
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

print(max_value)
print(min_value)