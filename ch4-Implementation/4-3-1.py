# 4-3 : 왕실의 나이트

m = input()
x = ord(m[0]) - 96
y = int(m[1])

result = 0

d1 = [-1, 1]
d2 = [-2, 2]

# 수평으로 한 칸 이동
for i in d1:
    for j in d2:
        if (x + i >= 1 and x + i <= 8 and y + j >= 1 and y + j <= 8):
            result += 1


# 수평으로 두 칸 이동
for i in d2:
    for j in d1:
        if (x + i >= 1 and x + i <= 8 and y + j >= 1 and y + j <= 8):
            result += 1

print(result)
