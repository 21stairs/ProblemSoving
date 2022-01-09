# https://www.acmicpc.net/problem/2578
def is_bingo():
    # 가로 세로 췍
    answer = 0
    for i in range(N):
        g_cnt = 0
        s_cnt = 0
        for j in range(N):
            if bingo[i][j] == 0:
                g_cnt += 1
            if bingo[j][i] == 0:
                s_cnt += 1
        else:
            if g_cnt == 5:
                answer += 1
            if s_cnt == 5:
                answer += 1
    # 대각 췍
    r_daegak = 0
    l_daegak = 0
    for r in range(N):
        if bingo[r][r] == 0:
            l_daegak += 1
        if bingo[r][N-1-r] == 0:
            r_daegak += 1
    else:
        if r_daegak == 5:
            answer += 1
        if l_daegak == 5:
            answer += 1

    if answer >= 3:
        return True
    return False


def where():
    for i in range(N):
        for j in range(N):
            for r in range(N):
                for c in range(N):
                    if bingo[r][c] == num[i][j]:
                        where_num[bingo[r][c]] = (r, c)



N = 5
bingo = [list(map(int, input().split())) for _ in range(N)]
num = [list(map(int, input().split())) for _ in range(N)]
where_num = [0] * 26
is_done = False
where()
for i in range(N):
    for j in range(N):
        y, x = where_num[num[i][j]]
        bingo[y][x] = 0
        if i >= 2:
            if is_bingo():
                print(i * 5 + j +1)
                is_done = True
                break
    if is_done:
        break
