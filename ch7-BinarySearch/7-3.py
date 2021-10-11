# 7-3 : 반복문으로 구현한 이진 탐색 소스코드

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)