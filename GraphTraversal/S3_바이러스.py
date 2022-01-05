# https://www.acmicpc.net/problem/2606
def DFS(idx):
    stack = [idx]
    while stack:
        idx = stack[-1]
        for arg in arr[idx]:
            if not visited[arg]:
                stack.append(arg)
                visited[arg] = 1
                break
        else:
            stack.pop()

    print(sum(visited) - 1)


N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)

DFS(1)