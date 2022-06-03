# https://www.acmicpc.net/problem/2156
N = int(input())
arr = []
dp = [0] * N
for _ in range(N):
    arr.append(int(input()))

if N == 1 or N == 2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
    print(max(dp))