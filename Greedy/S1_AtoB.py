# https://www.acmicpc.net/problem/16953

start, end = map(int, input().split())
cnt = 1
result = -1
# end가 스타트보다 작아지면 못 구하는 숫자임
while end >= start:
    # 1. 마지막이 1이면 빼고, 아니면 나누자
    if end == start:
        result = cnt
        break
    str_end = str(end)
    if str_end[-1] == '1':
        str_end.rstrip('1')
        end = int(str_end[:-1])
    elif str_end[-1] in ['3', '5', '7', '9']:
        break
    else:
        end //= 2
    cnt += 1

print(result)