# Ch 9-3 : 전보
# 다익스트라 알고리즘 사용
import heapq # 우선순위 큐
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 N, 간선의 개수 M, 출발 노드 C 입력받기
n, m, c = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 최단 시간 테이블을 모두 무한으로 초기화
time = [INF] * (n + 1)

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # 도시 X에서 Y로 메시지가 전달되는 시간 Z
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 시간은 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    time[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 시간이 짧은 노드에 대한 정보 꺼내기
        t, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if time[now] < t:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for g in graph[now]:
            cost = t + g[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < time[g[0]]:
                time[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

# 다익스트라 알고리즘 수행
dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 시간
max_time = 0

for t in time:
    if t != INF:
        count += 1
        max_time = max(max_time, t)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_time)