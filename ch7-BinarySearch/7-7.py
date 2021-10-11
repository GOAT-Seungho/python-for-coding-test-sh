# Ch 7-2 : 부품 찾기 (집합 자료형 이용)

# N : 부품의 개수
n = int(input())
components = set(map(int, input().split()))

# M : 손님이 주문한 부품의 개수
m = int(input())
orders = list(map(int, input().split()))

for o in orders:
    if o in components:
        print("yes", end=" ")
    else:
        print("no", end=" ")
print()