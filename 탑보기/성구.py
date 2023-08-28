''' 틀렸습니다
# 22866 탑 보기
import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
dp = [[] for _ in range(N)]
left_stack = []
right_stack = []

left = 0
right = N - 1
while left < N and right >= 0:
    if left_stack:
        while left_stack:
            if towers[left_stack[-1]] > towers[left]:
                break
            left_stack.pop()
    dp[left] += left_stack
    # dp[left].append(left_stack)
    left_stack.append(left)
    if right_stack:
        while right_stack:
            if towers[right_stack[-1]] > towers[right]:
                break
            right_stack.pop()
    # dp[right].append(right_stack)
    dp[right] += right_stack
    right_stack.append(right)

    left += 1
    right -= 1



for i in range(N):
    nearest = 100001
    for j in dp[i]:
        if abs(nearest - i) > abs(i - j):
            nearest = j
        elif abs(nearest - i) == abs(i - j):
            if nearest > j:
                nearest = j
    print(len(dp[i]), nearest + 1) if dp[i] else print(0)

'''