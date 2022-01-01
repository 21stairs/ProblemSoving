# https://www.acmicpc.net/problem/1343
def solve(cnt):
    global result
    result += 'AAAA' * (cnt // 4)
    cnt %= 4
    result += 'BB' * (cnt // 2)


poly = input()
result = ''
cnt = 0
for i in range(len(poly)):
    if poly[i] == 'X':
       cnt += 1
    else:
        solve(cnt)
        result += '.'
        cnt = 0
else:
    solve(cnt)
    cnt = 0

if len(result) != len(poly):
    result = -1
print(result)
