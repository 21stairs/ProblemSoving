# https://www.acmicpc.net/problem/1743
def dfs(r, c):
    global max_val
    visited[r][c] = 1
    stack = [(r, c)]
    cnt = 1
    while stack:
        cr, cc = stack[-1]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and trash[nr][nc]:
                visited[nr][nc] = 1
                cnt += 1
                stack.append((nr, nc))
                break
        else:
            stack.pop()
    max_val = max(max_val, cnt)


N, M, K = map(int, input().split())
trash = [[0] * M for _ in range(N+1)]
visited = [[0] * M for _ in range(N+1)]
max_val = 0
for _ in range(K):
    r, c = map(int, input().split())
    trash[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if trash[i][j] and not visited[i][j]:
            dfs(i, j)
print(max_val)