# Ch13-4 : 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058


# '균형잡힌 괄호 문자열'의 인덱스 반환
def balanced_index(string):
    cnt = 0 # 왼쪽 괄호의 개수
    for i in range(len(string)):
        if string[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

# '올바른 괄호 문자열'인지 판단
def check_proper(string):
    cnt = 0 # 왼쪽 괄호의 개수
    for s in string:
        if s == '(':
            cnt += 1
        else:
            if cnt == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            cnt -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if p == '':
        return answer
    
    # 2. 문자열을 "균형잡힌 문자열" u와 v로 분리한다.
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    # '올바른 괄호 문자열'이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # '올바른 괄호 문자열'이 아니라면, 아래의 과정을 수행
    else:
        answer = '(' + solution(v) + ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    
    return answer