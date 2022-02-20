# Ch14-1. 국영수
'''
1. 국어 점수가 감소하는 순서
2. 국어 점수가 같으면 영어 점수가 증가하는 순서
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (대문자는 소문자보다 작으므로 사전 순으로 앞에 온다.)
'''

n = int(input())
data = []
for i in range(n):
    temp = list(input().split())
    name = temp[0]
    language, english, math = int(temp[1]), int(temp[2]), int(temp[3])
    data.append((name, language, english, math))

data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0])
    