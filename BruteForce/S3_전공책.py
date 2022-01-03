# https://www.acmicpc.net/problem/16508
def solve(idx, pay):
    global min_pay
    # base case
    # 가격이 더 최소값보다 높으면 리턴
    if pay > min_pay:
        return
    # 찾는값과 같으면 리턴
    if idx == M:
        min_pay = pay
        return

    # idx는 find의 인덱스, i는 책과 가격의 인덱스
    for i in range(N):
        if find[idx] in books[i]:
            # replace 함수는 실제 값을 변경시키지는 않고 반환만 함.
            # (old, new, 몇개)
            books[i] = books[i].replace(find[idx], '!', 1)
            if not used[i]:
                used[i] = 1
                solve(idx+1, pay+prices[i])
                used[i] = 0
            else:
                solve(idx+1, pay)
            books[i] = books[i].replace('!', find[idx], 1)
    return


find = input()
N = int(input())
prices = []
books = []
used = [0] * N
M = len(find)
min_pay = 0xFFFFFF
for _ in range(N):
    price, book = input().split()
    prices.append(int(price))
    books.append(book)

solve(0, 0)
if min_pay == 0xFFFFFF:
    print(-1)
else:
    print(min_pay)
