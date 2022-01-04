# https://www.acmicpc.net/problem/16439
def calc():
    all_val = 0
    for i in range(N):
        val = 0
        for j in range(M):
            if selected[j]:
                val = max(val, chic[i][j])
        all_val += val
    return all_val


def solve(cnt, satis):
    global max_satis
    if satis > max_satis:
        max_satis = satis

    if cnt == 3:
        return

    for i in range(M):
        if not selected[i]:
            selected[i] = 1
            val = calc()
            solve(cnt+1, val)
            selected[i] = 0
        else:
            val = calc()
            solve(cnt+1, val)
    return


N, M = map(int, input().split())
chic = [list(map(int, input().split())) for _ in range(N)]
selected = [0] * M
max_satis = 0
solve(0, 0)
print(max_satis)