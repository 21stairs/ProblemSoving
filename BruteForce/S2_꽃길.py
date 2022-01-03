# https://www.acmicpc.net/problem/14620
def after(r, c):
    for i in range(5):
        nr, nc = r+dr[i], c+dc[i]
        if visited[nr][nc]:
            return False
    return True


def solve(seed, pay):
    global min_pay
    # base case
    # 비용이 최소비용을 넘을 때
    if pay >= min_pay:
        return
    # 3개의 꽃을 모두 심었을 때
    if seed == 3:
        min_pay = pay
        return

    # 1. 인덱스 조건 처리 2. 방문 처리(대각 3칸) 3. 계산(상하좌우)
    for i in range(1, N-1):
        for j in range(1, N-1):
            if after(i, j):
                fee = 0
                for di, dj in direction:
                    visited[i+di][j+dj] = 1
                    fee += ground[i+di][j+dj]
                solve(seed+1, pay+fee)
                for di, dj in direction:
                    visited[i+di][j+dj] = 0

N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]
direction = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0] * N for _ in range(N)]
min_pay = 0xFFFFFF
solve(0, 0)
print(min_pay)
