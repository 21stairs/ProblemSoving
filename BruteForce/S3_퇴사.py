# https://www.acmicpc.net/problem/14501
N = int(input())
table = [0] * N
dp = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())
    table[i] = (t, p)

for i in range(N):
    time, pay = table[i]
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if i+time <= N:
        if dp[i + time] < dp[i] + pay:
            dp[i+time] = dp[i] + pay
print(dp[-1])

