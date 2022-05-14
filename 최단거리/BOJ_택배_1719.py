v, e = map(int, input().split())
INF = 0xFFFF
arr = [[INF] * (v+1) for _ in range(v+1)]
answer = [['-'] * (v+1) for _ in range(v+1)]

for i in range(1, v+1):
    arr[i][i] = 0

for _ in range(e):
    i, j, k = map(int, input().split())
    arr[i][j] = k
    arr[j][i] = k
    answer[i][j] = j
    answer[j][i] = i

# i -> j => i -> k -> j
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                answer[i][j] = answer[i][k]

for i in range(1, v+1):
    # print(*answer[i][1:])
    print(answer[i])