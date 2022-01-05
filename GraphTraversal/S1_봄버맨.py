# https://www.acmicpc.net/problem/16918
def boom(r, c):
    for dr, dc in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r+dr, c+dc
        if 0<=nr<R and 0<=nc<C:
            data[nr][nc] = '.'


R, C, N = map(int, input().split())
data = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dinamite = []
# 1. o 폭탄 터뜨리기 => 다 위치 저장해놓기
# 2. . 폭탄 채우기

if N % 2:
    for c in range(1, N+1):
        if not c % 2: # 짝수일 때
            for i in range(R):
                for j in range(C):
                    if data[i][j] == '.':
                        data[i][j] = 'O'
        else:
            for r, c in dinamite:
                boom(r, c)
            dinamite = []
            for i in range(R):
                for j in range(C):
                    if data[i][j] == 'O':
                        dinamite.append((i, j))
    for i in range(R):
        print(''.join(data[i]))
else:
    for _ in range(R):
        print('O' * C)