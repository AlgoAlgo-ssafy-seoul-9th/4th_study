# 21921 백준_블로그

import sys
input = sys.stdin.readline

# 시간 초과
# N, X = map(int, input().split())
# visitors = list(map(int, input().split()))
# max = 0

# for i in range(0, N-X+1):
#     if sum(visitors[i : i+X]) > max:
#         max = sum(visitors[i : i+X])
#         cnt = 1
#     elif sum(visitors[i : i+X]) == max:
#         cnt += 1

# print(max)
# if max == 0:
#     print('SAD')
# else:
#     print(cnt)

# 2차 시도

N, X = map(int, input().split())
visitors = list(map(int, input().split()))
max = tmp = sum(visitors[:X])
cnt = 0

for i in range(X, N):
    tmp += visitors[i]
    tmp -= visitors[i-X]
    if tmp > max:
        max = tmp
        cnt = 1
    elif tmp == max:
        cnt += 1


if max == 0:
    print('SAD')
else:
    print(max)
    print(cnt)