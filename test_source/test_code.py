n = int(input())

meetings = []

for _ in range(n):
    start, end = map(int, input().split(" "))
    meetings.append((start, end))
# 醫낅즺 �쒓컙�� �ㅻ쫫李⑥닚 �뺣젹�섍퀬, �쒖옉 �쒓컙�� �ㅻ쫫李⑥닚 �뺣젹�⑸땲��
meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = 0
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1

print(answer)

import sys

input = sys.stdin.readline

N = int(input())

roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

# 泥ル쾲吏� 媛� �뷀븯湲�
min_price = roads[0] * costs[0]

# 媛��� 媛믪씠 �� 二쇱쑀�� 吏���
min_cost = costs[0]

for i in range(1, N - 1):
    if min_cost > costs[i]:  # 媛��� 媛믪씠 �� 二쇱쑀�뚭� �꾩옱 二쇱쑀�� 蹂대떎 鍮꾩떥硫� 諛붽퓭以���.
        min_cost = costs[i]  # 媛� �� 二쇱쑀�뚮줈 諛붽퓭二쇨린

    min_price += min_cost * roads[i]

print(min_price)

import sys
input = sys.stdin.readline

n, m = map(int, input().rsplit())
memories = list(map(int, input().rsplit()))
cost = list(map(int, input().rsplit()))

tc = sum(cost)
result = sys.maxsize

dp = [[0 for _ in range(tc+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(tc):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], memories[i] + dp[i-1][j-cost[i]])

        if dp[i][j] >= m:
            result = min(result, j)

if m==0:
    print(0)
elif n==1:
    print(cost[0])
elif result == sys.maxsize:
    print(n*m)
else:
    print(result)


import sys
sys.setrecursionlimit(10 ** 8)

N, M = map(int, sys.stdin.readline().split())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * (M) for _ in range(N)]
dp[N - 1][M - 1] = 1

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y, W, dp):
    if dp[y][x] != -1:
        return dp[y][x]

    tmp = 0
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < M and 0 <= ny < N and W[y][x] > W[ny][nx]:
            tmp += dfs(nx, ny, W, dp)
    dp[y][x] = tmp

    return dp[y][x]
print(dfs(0, 0, W, dp))