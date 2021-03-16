# 신나는 함수 실행 (DP 연습)
# 틀린 문제 (꼭 다시 풀어볼 것!)

import sys

# DP를 위한 저장소 생성
memo = {}

# DP 함수식 구현
def dp(t, memo):
    if t in memo:
        return memo[t]

    if t[0] <= 0 or t[1] <= 0 or t[2] <= 0:
        return 1

    if t[0] > 20 or t[1] > 20 or t[2] > 20:
        return memo[(20, 20, 20)]
    
    if t[0] < t[1] < t[2]:
        new_t = dp((t[0], t[1], t[2]-1), memo) + dp((t[0], t[1]-1, t[2]-1), memo) - dp((t[0], t[1]-1, t[2]), memo)
        return new_t

    else:
        new_t = dp((t[0]-1, t[1], t[2]), memo) + dp((t[0]-1, t[1]-1, t[2]), memo) + dp((t[0]-1, t[1], t[2]-1), memo) - dp((t[0]-1, t[1]-1, t[2]-1), memo)
        return new_t

    memo[t] = new_t

while True:
    t = tuple(map(int,sys.stdin.readline().strip().split()))

    if t[0]== -1 and t[1] == -1 and t[2] == -1:
        break

    print(dp(t, memo))


#  다른 풀이
