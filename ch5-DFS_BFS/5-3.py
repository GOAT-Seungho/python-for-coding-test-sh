# 5-3 : 음료수 얼려 먹기

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 현재 노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우 재귀 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else:
        return False


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
