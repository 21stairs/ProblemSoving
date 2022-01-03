# https://www.acmicpc.net/problem/2798
# 조합문제
def solve(num, s, cnt):
    global max_val
    if num > M:
        return
    if cnt == 3:
        max_val = max(num, max_val)
        return

    for i in range(s, N+cnt-2):
        solve(num+cards[i], i+1, cnt+1)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_val = 0
solve(0, 0, 0)
print(max_val)

