# Ch 7-2 : 부품 찾기 (이진 탐색)

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        
        # 중간점의 값보다 target 값이 작은 경우
        elif array[mid] > target:
            end = mid - 1
        
        # 중간점의 값보다 target 값이 큰 경우
        else:
            start = mid + 1
    return None

# N : 부품의 개수
n = int(input())
components = list(map(int, input().split()))
components.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

# M : 손님이 주문한 부품의 개수
m = int(input())
orders = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for o in orders:
    # 해당 부품이 존재하는지 확인
    result = binary_search(components, o, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')

print()