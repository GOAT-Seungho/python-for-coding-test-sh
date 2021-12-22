# 11-3 : 무자열 뒤집기

s = input()
count = 0 # 0과 1이 번갈아 나오는 횟수

now = s[0]
for i in range(1, len(s)):
    if now != s[i]:
        count += 1
        now = s[i]

result = count // 2 + count % 2
print(result)


# 교재 답안

# data = input()
# count0 = 0 # 전부 0으로 바꾸는 경우
# count1 = 0 # 전부 1로 바꾸는 경우

# # 첫 번째 원소에 대해서 처리
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1

# # 두 번째 원소부터 모든 원소를 확인하며
# for i in range(len(data) - 1):
#     if data[i] != data[i+1]:
#         # 다음 수에서 1로 바뀌는 경우
#         if data[i + 1] == '1':
#             count0 += 1
#         # 다음 수에서 0으로 바뀌는 경우
#         else:
#             count1 += 1

# print(min(count0, count1))