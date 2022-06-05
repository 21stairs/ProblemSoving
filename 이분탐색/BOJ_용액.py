# https://www.acmicpc.net/problem/2467
import sys

N = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
min_gap = 2e9
l, r = 0, N-1
answer = ()
while l < r:
    char_val = data[l]+data[r]
    if abs(char_val) <= min_gap:
        min_gap = abs(char_val)
        answer = (data[l], data[r])
    if char_val == 0:
        break
    elif char_val > 0:
        r -= 1
    else:
        l += 1
print(*answer)