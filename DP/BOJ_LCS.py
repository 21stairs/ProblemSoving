# https://www.acmicpc.net/problem/9251
a = input()
b = input()

N = len(a)
M = len(b)

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N-1][M-1])