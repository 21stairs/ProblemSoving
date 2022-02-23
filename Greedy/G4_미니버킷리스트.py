# https://www.acmicpc.net/problem/24270
N, K = map(int, input().split())
Sn = list(map(int, input().split()))
result = 1
val = K-sum(Sn)+N
for i in range(N):
    result = result * (val-i) % 1000000007

print(result)