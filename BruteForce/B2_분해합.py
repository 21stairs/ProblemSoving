# https://www.acmicpc.net/problem/2231

N = int(input())
for i in range(N):
    result = i
    num = i
    while num:
        result += num % 10
        num //= 10
    if result == N:
        print(i)
        break
else:
    print(0)

