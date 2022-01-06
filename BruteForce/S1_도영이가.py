# https://www.acmicpc.net/problem/1548
def solve():
    min_val = 0xFFFF
    for i in range(1, 2**N):
        sour = 1
        bitter = 0
        for j in range(N):
            if i & (1 << j):
                sour *= tasty[j][0]
                bitter += tasty[j][1]
        min_val = min(min_val, abs(sour-bitter))
    return min_val

N = int(input())
# 신맛=> 곱 쓴맛=> 합
tasty = [list(map(int, input().split())) for _ in range(N)]
print(solve())
