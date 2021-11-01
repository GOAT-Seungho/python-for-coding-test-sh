# Ch 9-2 : 미래 도시
# 플로이드 워셜 알고리즘 사용
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 N, 간선의 개수 M 입력
n, m = map(int, input().split())

# 2차원 리스트 생성 후 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 경우 0 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # from, to
    f, t = map(int, input().split())
    graph[f][t] = 1
    graph[t][f] = 1

# 최종 목적지 X, 거쳐 가야할 곳 K 입력
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)