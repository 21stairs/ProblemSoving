# https://www.acmicpc.net/problem/13305

N = int(input())
dist = list(map(int, input().split()))
pay = list(map(int, input().split()))

min_pay = pay[0]
dis = 0
result = 0

for i in range(N-1):
    if min_pay > pay[i]:
        result += min_pay * dis
        min_pay = pay[i]
        dis = 0
    dis += dist[i]
else:
    result += min_pay * dis

print(result)