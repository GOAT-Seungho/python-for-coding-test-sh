# Ch13-3 : 경쟁적 전염

from collections import deque

# N: 행과 열의 크기, K: 바이러스의 가지 수
n, k = map(int, input().split())

graph = [] # N * N 크기의 2차원 그래프 입력받기
virus = [] # 바이러스에 대한 정보를 담는 리스트
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            virus.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
virus.sort()
q = deque(virus)

# S, X, Y: S초 뒤에 (X, Y)에 존재하는 바이러스의 종류 출력
target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])