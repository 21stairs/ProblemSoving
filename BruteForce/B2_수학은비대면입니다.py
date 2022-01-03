# https://www.acmicpc.net/problem/19532
a, b, c, d, e, f = map(int, input().split())

def solve():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                return x, y

x, y = solve()
print(x, y)

