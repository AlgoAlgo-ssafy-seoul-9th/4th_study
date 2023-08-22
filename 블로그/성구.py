# 21921 블로그
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visited = list(map(int, input().split()))

if max(visited):
    cnt = 1
    maxV = accum = sum(visited[0:X])
    for i in range(X, N):
        accum -= visited[i-X]
        accum += visited[i]
        if maxV < accum:
            maxV = accum
            cnt = 1
        elif maxV == accum:
            cnt += 1
    print(maxV)
    print(cnt) 

else:
    print('SAD')

'''
import sys

input = sys.stdin.readline
# input
N, X = map(int, input().split())
visited = list(map(int, input().split()))

# define
i, j = 0, X - 1
accum = sum(visited[i : j + 1])
maxV = cnt = 0
# sliding window
while j < N:
    if maxV < accum:
        cnt = 1
        maxV = accum
    elif maxV == accum:
        cnt += 1
    accum -= visited[i]
    i += 1
    j += 1
    if j >= N:
        break
    accum += visited[j]
if maxV:
    print(maxV)
    print(cnt)
else:
    print("SAD")
'''