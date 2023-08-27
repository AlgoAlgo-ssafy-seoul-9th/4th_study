# 2531_회전초밥_conveyor-belt sushi
import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = deque()
sushi_dict = {}
ans = deque()

cnt = 0
max_cnt = 0
length = 0

sushi_dict[c] = 0
for _ in range(N):
    s = int(input())
    sushi.append(s)
    if s in sushi_dict.keys():
        continue
    else:
        sushi_dict[s] = 0

for i in range(N+k):
    if sushi_dict[sushi[i % N]] == 0:
        cnt += 1
    sushi_dict[sushi[i % N]] += 1
    ans.append(sushi[i % N])
    length += 1
    if length < k:
        continue
    else:
        temp = cnt
        if sushi_dict[c] == 0:
            temp += 1
        if temp > max_cnt:
            max_cnt = temp
        now = ans.popleft()
        sushi_dict[now] -= 1
        if sushi_dict[now] == 0:
            cnt -= 1
        length -= 1

print(max_cnt)
