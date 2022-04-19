# 시험지를 K개의 그룹으로 나눈뒤 각각의 그룹에서 맞츤 문제 개수의 합을 구하여
# 최소값을 시험점수로 최대 점수를 계산하는 프로그램을 작성하자
import sys

N, K = map(int, input().split())
prob = list(map(int, sys.stdin.readline().rstrip().split()))

group = [[] for _ in range(K)]

# 어떻게 K개로 나눌것인가...