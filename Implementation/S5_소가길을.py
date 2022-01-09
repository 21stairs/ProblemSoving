# https://www.acmicpc.net/problem/14467

N = int(input())
cow_pos = [-1] * 11
across = [0] * 10

for _ in range(N):
    cow, pos = map(int, input().split())

    if cow_pos[cow] == -1:
        cow_pos[cow] = pos
    elif cow_pos[cow] != pos:
        cow_pos[cow] = pos
        across[cow-1] += 1

print(sum(across))
