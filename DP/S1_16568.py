# https://www.acmicpc.net/problem/16568

N, A, B = map(int, input().split())
DP = [123456789] * (N+1)
DP[0] = 0
# nums = [A+1, B+1, 1]
# nums.sort()
#
# for num in nums:
#     for j in range(num, N+1):
#         if DP[j-num] != 123456789:
#             DP[j] = min(DP[j-num]+1, DP[j])
# print(DP[-1])


dp = [x for x in range(N+1)]
for i in [A+1, B+1]:
    for j in range(i, N+1):
        dp[j] = min(dp[j], dp[j-i]+1)
    print(dp)