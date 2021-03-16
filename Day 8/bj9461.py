# 파도반 수열 (DP 연습)
# 맞은 문제
# DP list로 푸는 코드도 봐 두자

import sys

memo = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2
}

def dp(n):
    global memo

    if n in memo.keys():
        return memo[n]
    
    nth = dp(n-1) + dp(n-5)
    memo[n] = nth
    return nth

case = int(sys.stdin.readline().strip())
for _ in range(case):
    N = int(sys.stdin.readline().strip())
    print(dp(N))
    

