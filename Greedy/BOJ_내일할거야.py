import sys
N = int(input())
task = []
for _ in range(N):
    time, deadline = map(int, sys.stdin.readline().rstrip().split())
    task.append((time, deadline))

task.sort(key=lambda x: -x[1])
cur_day = task[0][1]

for time, dl in task:
    # 1. 현재 날짜가 데드라인보다 앞뒤인지 확인해야함.
    if cur_day > dl:
        cur_day = dl
    # 2. 앞이면 현재날짜부터 소요시간을 차감해주고,
    cur_day -= time
    # 3. 뒤면 현재값에 데드라인을 넣어주고 소요시간을 차감해준다.
    # 4. 끝났을 때 날짜를 구하면된다.
print(cur_day)