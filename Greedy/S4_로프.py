N = int(input())
rope = []
max_weight = 0
for _ in range(N):
    rope.append(int(input()))
#
# for i in range(1, 2**N):
#     sub = []
#     for j in range(N):
#         idx = i & (1 << j)
#         if idx:
#             sub.append(rope[idx-1])
#     max_weight = max(min(sub)*len(sub), max_weight)
#
# print(max_weight)
rope.sort()
for i in range(N):
    cur = rope[i] * (N-i)
    max_weight = max(cur, max_weight)
print(rope)
print(max_weight)