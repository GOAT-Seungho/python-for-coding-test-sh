# 4-2 : 시각

n = int(input())

three = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]  # 15

result = 0

for i in range(n+1):
    if (i in three):
        result += 3600
    else:
        result += 1575

print(result)
