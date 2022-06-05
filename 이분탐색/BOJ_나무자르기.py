# https://www.acmicpc.net/problem/2805
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

l, r = 0, max(trees)

while l <= r:
    mid = (l+r) // 2
    rest = 0
    for tree in trees:
        if tree > mid:
            rest += tree - mid
            if rest > M:
                break
    # 너무 많이 깎았음
    if rest >= M:
        l = mid+1
    else:
        r = mid-1
print(r)