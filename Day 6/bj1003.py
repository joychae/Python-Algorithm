# 피보나치 함수 (동적계획법 연습)
# 맞은 문제

import sys

case = int(sys.stdin.readline().strip())

# DP를 위한 저장소 생성
memo_0 = {
    0: 1,
    1: 0
}

memo_1 = {
    0: 0,
    1: 1
}

# DP 함수식 구현
def dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = dynamic_programming(n - 1, fibo_memo) + dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

case_list = []
for _ in range(case):
    input = int(sys.stdin.readline().strip())
    case_list.append(input)

for case in case_list:
    print(dynamic_programming(case, memo_0),dynamic_programming(case,memo_1))


