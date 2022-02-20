# 14-3. 실패율

'''
- 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
- N: 전체 스테이지의 수 (1 <= N <= 500)
- stages: 게임을 이용하는 사용자가 현재 멈춰잇는 스테이지의 번호가 담긴 배열 (1 <= len(stages) <= 200,000)
    - stages에는 1 이상 N+1 이하의 자연수가 담겨 있다.
    - N+1은 마지막 스테이지까지 클리어한 사용자를 말한다.
- 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 한다.
- 스테이지에 도달한 유저가 없는 경우 실패율은 0으로 정의한다.

-> 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열 반환하라 !

eg. N = 5, stages = [2, 1, 2, 6, 2, 4, 3, 3] -> result = [3, 4, 2, 1, 5]

[1, 2, 2, 2, 3, 3, 4, 6]

1 -> 1/8
2 -> 3/7
3 -> 2/4
4 -> 1/2
5 -> 0/1 


eg. N = 4, stages = [4, 4, 4, 4, 4] -> result = [4, 1, 2, 3]
1 -> 0/5
2 -> 0/5
3 -> 0/5
4 -> 5/5
'''

def solution(N, stages):
    stages.sort()
    temp = []

    for i in range(1, N+1):
        total = len(stages)
        now = stages.count(i)
        del stages[:now]
        if total == 0:
            temp.append((i, 0))
        else:
            temp.append((i, now / total))

    temp.sort(key=lambda x: x[1], reverse=True)

    answer = [temp[i][0] for i in range(N)]

    return answer





N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))