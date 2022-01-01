# 12-4 : 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 교재 답안

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False

    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return False



# numpy 사용
# import numpy as np
# import copy

# def solution(key, lock):
#     answer = False
    
#     # numpy 형식으로 변경
#     key = np.array(key)
#     lock = np.array(lock)
    
#     # 늘려줄 자물쇠의 크기 : 기존 자물쇠의 3배
#     length = len(lock) * 3
#     new_lock = np.zeros((length, length))
    
#     # 늘려준 자물쇠의 중앙 부분에 원래 자물쇠를 넣어준다.
#     new_lock[len(lock):len(lock)*2, len(lock):len(lock)*2] = lock
    
#     # 자물쇠의 모든 홈이 채워진 것을 의미하는 1로 채워진 행렬
#     one_list = np.ones((len(lock), len(lock)))
    
    
#     for r in range(len(key) + 1):
#         key_tok = np.rot90(key, r)

#         for i in range(1, len(lock) * 2):
#             for j in range(1, len(lock) * 2):
#                 new_lock[i:i+len(key), j:j+len(key)] += key_tok

#                 # 모두 1인 행렬과 비교
#                 temp = new_lock[len(lock):len(lock) * 2, len(lock):len(lock) * 2]
#                 if temp.min() == temp.max():
#                 # if np.array_equal(one_list, new_lock[len(lock):len(lock) * 2, len(lock):len(lock) * 2]):
#                     return True
#                 else:
#                     new_lock[i:i+len(key), j:j+len(key)] -= key_tok
    
#     return answer