import sys

n = int(sys.stdin.readline().strip())
dp = [0]*1000001
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = ((dp[i-1] % 15746) + (dp[i-2] % 15746))%15746
print(dp[n])

# # DP를 위한 저장소 생성
# import sys

# memo = {
#     0: 1,
#     1: 2
# }

# # DP 함수식 구현
# def dynamic_programming(n, fibo_memo):
#     if n in fibo_memo:
#         return fibo_memo[n]

#     nth_fibo = dynamic_programming(n - 1, fibo_memo) + dynamic_programming(n - 2, fibo_memo)
#     fibo_memo[n] = nth_fibo
#     return nth_fibo

# n = int(sys.stdin.readline().strip())

# print(dynamic_programming(n-1,memo))