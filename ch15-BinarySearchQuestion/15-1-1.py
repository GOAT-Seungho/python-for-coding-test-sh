# 15-1. 정렬된 배열에서 특정 수의 개수 구하기
# bisect 라이브러리 미사용

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    pass


n, x = map(int, input().split())
data = list(map(int, input().split()))

result = data.count(x)

if result == 0:
    print(-1)
else:
    print(result)