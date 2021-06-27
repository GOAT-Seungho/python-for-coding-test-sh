# 4-1 : 상하좌우

N = int(input())
move = list(input().split())

x = y = 1

for m in move:
    if m == 'L':
        if y != 1:
            y -= 1

    elif m == 'R':
        if y != N:
            y += 1

    elif m == 'U':
        if x != 1:
            x -= 1

    elif m == 'D':
        if x != N:
            x += 1

print(x, y)
