# 2531 회전초밥
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# input
N, d, k, c = map(int, input().split())
sushies = [int(input()) for _ in range(N)]

# define
kind = defaultdict(int)

i, j = 0, k
event_sushies = deque(sushies[0:k])
for idx in event_sushies:
    kind[idx] += 1
# 종류 개수의 최댓값
max_kind = len(kind.keys())

# window slice
while i < N:
    poped = event_sushies.popleft()
    kind[poped] -= 1
    if not kind[poped]:
        kind.pop(poped)
    event_sushies.append(sushies[j])
    kind[sushies[j]] += 1
    if c in kind.keys():
        max_kind = max(max_kind, len(kind.keys()))
    else:
        max_kind = max(max_kind, len(kind.keys())+1)
    i += 1
    # 회전 큐를 만들기 위해서 마지막 인덱스에서 추가되면 초기값으로 돌아감
    j = (j+1)%N

print(max_kind)
        

'''
# 2531 회전초밥
import sys
from collections import deque
input = sys.stdin.readline

def kindLen(lst, element):
  
    return len(set(lst)) if element in lst else len(set(lst))+1

N, d, k, c = map(int, input().split())
sushies = [int(input()) for _ in range(N)]
i, j = 0, k
event_sushies = deque(sushies[0:k])
max_kind = kindLen(event_sushies, c)
while i < N:
    event_sushies.popleft()
    event_sushies.append(sushies[j])
#  print(i, j, "i와 j")
#  print(event_sushies, "event_")

    max_kind = max(max_kind, kindLen(event_sushies, c))
    i += 1
    j = (j+1)%N

print(max_kind)
'''