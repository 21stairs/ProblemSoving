# https://www.acmicpc.net/problem/5567
from collections import deque

N = int(input())
m = int(input())
friends = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
queue = deque([(1, 0)])
visited[1] = 1
cnt = 0
while queue:
    idx, depth = queue.popleft()
    if depth == 2:
        break
    for friend in friends[idx]:
        if not visited[friend]:
            cnt += 1
            visited[friend] = 1
            queue.append((friend, depth+1))
print(cnt)