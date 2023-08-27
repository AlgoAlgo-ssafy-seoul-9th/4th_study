# 22866_탑보기_View the Tower
import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []
# [탑개수, 가까운탑위치, 가까운탑거리]
ans = [[0, 0, float('inf')] for _ in range(N)]
length_of_stack = 0
for i in range(N):
    while length_of_stack > 0 and stack[-1][1] <= towers[i]:
        stack.pop()
        length_of_stack -= 1
    ans[i][0] += length_of_stack

    if stack:
        dis = abs(i - stack[-1][0])
        if dis < ans[i][2]:
            ans[i][1] = (stack[-1][0]+1)
            ans[i][2] = dis
        elif dis == ans[i][2]:
            ans[i][1] = min((stack[-1][0]+1),ans[i][1])
    stack.append([i, towers[i]])
    length_of_stack += 1

stack.clear()
length_of_stack = 0

for i in range(N-1, -1, -1):
    while length_of_stack > 0 and stack[-1][1] <= towers[i]:
        stack.pop()
        length_of_stack -= 1
    ans[i][0] += length_of_stack

    if stack:
        dis = abs(i - stack[-1][0])
        if dis < ans[i][2]:
            ans[i][1] = (stack[-1][0]+1)
            ans[i][2] = dis
        elif dis == ans[i][2]:
            ans[i][1] = min((stack[-1][0]+1),ans[i][1])
    stack.append([i, towers[i]])
    length_of_stack += 1


for v in ans:
    if v[0] == 0:
        print(0)
    else:
        print(v[0],v[1])