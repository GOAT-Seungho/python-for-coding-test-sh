# 예제 3-1 거스름돈

# 500, 100, 50, 10
# N원 -> 동전의 최소 개수

N = int(input())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += N // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    N %= coin

print(count)