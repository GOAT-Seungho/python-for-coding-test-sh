# Ch 7-2 : 부품 찾기 (계수 정렬)

# N : 부품의 개수
n = int(input())
components = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    components[int(i)] = 1

# M : 손님이 주문한 부품의 개수
m = int(input())
orders = list(map(int, input().split()))

for o in orders:
    if components[o] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
print()