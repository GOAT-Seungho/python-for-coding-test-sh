# 12-1 : 럭키 스트레이트

n = input()
mid = int(len(n)/2)
left = 0
right = 0

for i in range(mid):
    left += int(n[i])
    right += int(n[mid+i])

print("LUCKY") if left == right else print("READY")