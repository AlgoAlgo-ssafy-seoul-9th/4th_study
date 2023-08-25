# 21921_블로그_blog
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

now_sum = sum(visitors[0:X])
max_visitor = now_sum
duration = 1
for i in range(X, N):
    temp = now_sum+visitors[i]-visitors[i-X]
    now_sum = temp
    if temp > max_visitor:
        max_visitor = temp
        duration = 1
    elif temp == max_visitor:
        duration += 1
    else:
        continue

if max_visitor == 0:
    print('SAD')
else:
    print(max_visitor)
    print(duration)