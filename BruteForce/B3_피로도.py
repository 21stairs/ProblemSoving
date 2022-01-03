# https://www.acmicpc.net/problem/22864

# input A: 피로도 증가량, B: 처리량, C: 피로도 감소량, M: 최대 피로도 ;

A, B, C, M = map(int, input().split())
tired = 0
work = 0
for i in range(24):
    if tired + A > M:
        tired = tired-C if tired < 0 else 0
    else:
        work += B
        tired += A
print(work)

