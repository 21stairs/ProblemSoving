# https://www.acmicpc.net/problem/14248

N = int(input())
bridge = list(map(int, input().split()))
start = int(input()) - 1
visited = [0] * N
stack = [start]
visited[start] = 1

while stack:
    cur_idx = stack.pop()
    l_idx = cur_idx - bridge[cur_idx]
    r_idx = cur_idx + bridge[cur_idx]
    if 0 <= l_idx < N and not visited[l_idx]:
        visited[l_idx] = 1
        stack.append(l_idx)
    if 0 <= r_idx < N and not visited[r_idx]:
        visited[r_idx] = 1
        stack.append(r_idx)

print(sum(visited))