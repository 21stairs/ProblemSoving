# https://www.acmicpc.net/problem/12865
# def solve(value, weight, idx):
#     global result
#     if weight > K:
#         return
#     if idx == N:
#         result = max(result, value)
#         return
#
#     solve(value+stuff[idx][1], weight+stuff[idx][0], idx+1)
#     solve(value, weight, idx+1)
#     solve(0, 0, 0)

N, K = map(int, input().split())
stuff = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    stuff.append((W, V))
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W = stuff[i][0]
        V = stuff[i][1]
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-W] + V, dp[i-1][j])
print(max(dp[-1]))



# 부분집합 => 시간초과
# for i in range(1, 1 << N):
#     wei = 0
#     val = 0
#     for j in range(N):
#         if i & 1 << j:
#             wei += weight[j]
#             val += value[j]
#     if wei <= K:
#         result = max(result, val)

# 재귀로 풀면될거같은데 N < 100이니까 최대 Depth가 100 이하니까 최대재귀깊이 안

