# 4-4 : 게임 개발

# 입력 예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# N * M 으로 이루어진 직사각형
m, n = map(int, input().split())

# (A, B) : 좌표, d : 방향 (0 : 북, 1 : 동, 2 : 남, 3: 서)
a, b, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

pos = (a, b)
result = 1          # 처음 있는 장소 카운트
game_map[a][b] = 1  # 처음 서 있는 장소 들리지 못하는 곳으로 변경
rotate = 0      # 방향만 회전하는 경우 카운트

while True:
    if rotate == 4:
        break

    rotate += 1
    if d == 0:       # 북을 바라보고 있을 때
        d = 3        # 서를 바라본다.
        # 서쪽에 붙어있지 않고, 서쪽으로 한 칸 갔을 때 그 곳이 육지인 경우
        if pos[1] != 0 and game_map[pos[0]][pos[1] - 1] == 0:
            result += 1
            pos = (pos[0], pos[1] - 1)
            game_map[pos[0]][pos[1]] = 1
            rotate = 0

    elif d == 3:     # 서를 바라보고 있을 때
        d = 2        # 남을 바라본다.
        # 남쪽에 붙어있지 않고, 남쪽으로 한 칸 갔을 때 그 곳이 육지인 경우
        if pos[0] != n-1 and game_map[pos[0] + 1][pos[1]] == 0:
            result += 1
            pos = (pos[0] + 1, pos[1])
            game_map[pos[0]][pos[1]] = 1
            rotate = 0

    elif d == 2:     # 남을 바라보고 있을 때
        d = 1        # 동을 바라본다.
        # 동쪽에 붙어있지 않고, 동쪽으로 한 칸 갔을 때 그 곳이 육지인 경우
        if pos[1] != m-1 and game_map[pos[0]][pos[1] + 1] == 0:
            result += 1
            pos = (pos[0], pos[1] + 1)
            game_map[pos[0]][pos[1]] = 1
            rotate = 0

    else:            # 동을 바라보고 있을 때
        d = 0        # 북을 바라본다.
        # 북쪽에 붙어있지 않고, 북쪽으로 한 칸 갔을 때 그곳이 육지인 경우
        if pos[0] != 0 and game_map[pos[0]-1][pos[1]] == 0:
            result += 1
            pos = (pos[0] - 1, pos[1])
            game_map[pos[0]][pos[1]] = 1
            rotate = 0

print(result)
