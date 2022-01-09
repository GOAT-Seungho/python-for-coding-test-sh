# 12-7 : 치킨 배달

from itertools import combinations

n, max_m = map(int, input().split())
graph = []
houses = []
chickens = []

for r in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

for r in range(n):
    for c in range(n):
        if graph[r][c] == 2: # 치킨집
            chickens.append((r, c))
        if graph[r][c] == 1: # 집
            houses.append((r, c))

dists = [[0] * len(chickens) for _ in range(len(houses))]
for r in range(len(houses)):
    for c in range(len(chickens)):
        dists[r][c] = abs(houses[r][0] - chickens[c][0]) + abs(houses[r][1] - chickens[c][1])

city_dists = [] # 치킨집 개수 별 도시의 치킨 거리 리스트
for m in range(max_m):
    comb_stores = list(combinations([i for i in range(len(chickens))], m + 1)) # 치킨집 m개의 조합
    
    dists_by_comb_stores = [] # 치킨집 m개의 조합에 따른 치킨 거리 리스트
    for stores in comb_stores:
        min_dists_by_houses = [] # 각 집 별 치킨 거리 리스트
        for h in range(len(houses)):
            dists_by_house = []
            for store in stores:
                dists_by_house.append(dists[h][store])
            min_dists_by_houses.append(min(dists_by_house))
        dists_by_comb_stores.append(sum(min_dists_by_houses))
    city_dists.append(min(dists_by_comb_stores))

print(min(city_dists))


# 교재 답안
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨 집

# 모든 치킨 집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)