# 12-5 : 뱀
# https://www.acmicpc.net/problem/3190

import copy

# N * N 보드 (0 : 길, 1 : 사과)
n = int(input())
# 보드 0으로 초기화
board = [[0] * n for _ in range(n)]

# K : 사과의 개수
k = int(input())
# 사과가 있는 위치에 9를 넣어준다.
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 9

# L : 뱀의 방향 전환 횟수
l = int(input())
turns = []
for _ in range(l):
    tok = list(input().split())
    turns.append([int(tok[0]), tok[1]])

# 뱀위 위치 정보
snake = [[0, 0]]
# 총 걸린 시간
count = 0
# 현재 뱀의 머리가 있는 칸은 1로 지정한다.
board[snake[0][0]][snake[0][1]] = 1
# 처음에 오른쪽을 향한다.
dx, dy = 0, 1

breaker = False

for turn in turns:
    time = turn[0]
    direction = turn[1]

    while count < time:
        count += 1

        x, y = snake[0][0], snake[0][1]
        
        # 탈출 조건 : 벽 또는 자기 자신의 몸과 부딪히면 게임 종료
        if x + dx == n or x + dx == -1 or \
           y + dy == n or y + dy == -1 or \
           board[x + dx][y + dy] == 1:
            breaker = True
            break
        
        # 다음 칸에 사과가 없다면,
        if board[x + dx][y + dy] == 0:
            board[snake[-1][0]][snake[-1][1]] = 0
            for i in range(len(snake)-1, 0, -1):
                snake[i] = copy.deepcopy(snake[i-1])
            snake[0][0] += dx
            snake[0][1] += dy
        
        # 만약 다음 칸에 사과가 있다면,
        else:
            snake.insert(0, [x + dx, y + dy])

        # 뱀의 위치 정보에 따른 보드 업데이트
        board[snake[0][0]][snake[0][1]] = 1
    
    if breaker:
        break

    # 시간이 지나면 방향 변경
    # L : 왼쪽으로 90도 회전
    if direction == 'L':
        if dx == 1:         # 아래쪽 -> 오른쪽
            dx, dy = 0, 1
        elif dx == -1:      # 위쪽 -> 왼쪽
            dx, dy = 0, -1
        elif dy == 1:       # 오른쪽 -> 위쪽
            dx, dy = -1, 0
        else:               # 왼쪽 -> 아래쪽
            dx, dy = 1, 0
    # R : 오른쪽으로 90도 회전
    else:
        if dx == 1:         # 아래쪽 -> 왼쪽
            dx, dy = 0, -1
        elif dx == -1:      # 위쪽 -> 오른쪽
            dx, dy = 0, 1
        elif dy == 1:       # 오른쪽 -> 아래쪽
            dx, dy = 1, 0
        else:               # 왼쪽 -> 위쪽
            dx, dy = -1, 0


while not breaker:
    count += 1

    x, y = snake[0][0], snake[0][1]
    # 탈출 조건 : 벽 또는 자기 자신의 몸과 부딪히면 게임 종료
    if x + dx == n or x + dx == -1 or \
        y + dy == n or y + dy == -1 or \
        board[x + dx][y + dy] == 1:
        breaker = True
        break
    
    # 다음 칸에 사과가 없다면,
    if board[x + dx][y + dy] == 0:
        board[snake[-1][0]][snake[-1][1]] = 0
        for i in range(len(snake)-1, 0, -1):
            snake[i] = copy.deepcopy(snake[i-1])
        snake[0][0] += dx
        snake[0][1] += dy
    
    # 만약 다음 칸에 사과가 있다면,
    else:
        snake.insert(0, [x + dx, y + dy])

    # 뱀의 위치 정보에 따른 보드 업데이트
    board[snake[0][0]][snake[0][1]] = 1

print(count)



# 교재 답안
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보 (사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로 (동, 서, 남, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1     # 뱀의 머리 위치
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0   # 처음에는 동쪽을 보고 있음
    time = 0        # 시작한 뒤에 지난 '초' 시간
    index = 0       # 다음에 회전할 정보
    q = [(x, y)]    # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1

        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전'
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())