# 15-1. 정렬된 배열에서 특정 수의 개수 구하기
# bisect 라이브러리 사용

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

result = bisect_right(data, x) - bisect_left(data, x)

if result == 0:
    print(-1)
else:
    print(result)
