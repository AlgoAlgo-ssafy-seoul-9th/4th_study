# 2531 백준_회전초밥

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
# N : 회전 초밥 벨트에 놓인 접시의 수
# d : 초밥의 가짓수
# k : 연속해서 먹는 접시의 수
# c : 쿠폰 번호
belts = []
for _ in range(N):
    belts.append(int(input()))
for i in range(k):
    belts.append(belts[i])
max = 0
for i in range(N):
    sushi = set(belts[i:i+k])
    if max <= len(sushi):
        max = len(sushi)
        if c in sushi:
            ans = len(sushi)
        else:
            ans = len(sushi)+1

print(ans)