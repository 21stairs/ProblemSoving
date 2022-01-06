# https://www.acmicpc.net/problem/14712
# Python3 로는 시간초과 발생(통과한사람이 단 2명) => PyPy3로는 통과
def solve(i, j):
    global cnt
    # base case
    if i >= 1 and j >= 1:
        if nemo[i][j] and nemo[i-1][j] and nemo[i][j-1] and nemo[i-1][j-1]:
            return
    cnt += 1
    while True:
        if j >= M:
            i += 1
            j = 0
            continue
        elif i >= N:
            break
        if not nemo[i][j]:
            nemo[i][j] = 1
            solve(i, j)
            nemo[i][j] = 0

        j += 1


N, M = map(int, input().split())
nemo = [[0] * M for _ in range(N)]
cnt = 0
solve(0, 0)
print(cnt)
