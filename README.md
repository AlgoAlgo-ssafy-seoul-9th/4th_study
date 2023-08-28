# 4th_study

[4주차] 코딩테스트 준비 4주차
<br/>

[프로그래머스 메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411)

[백준 문제집 바로가기](https://www.acmicpc.net/workbook/view/16614)

<br/><br/>

# [프로그래머스] 메뉴 리뉴얼

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./메뉴%20리뉴얼/성구.py)

```py
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    # default 타입을 지정가능한 dictionary(int => 0)
    dic_menus = defaultdict(int)
    # 코스 요리 메뉴 개수
    for length in course:
        # 새로운 메뉴 개수 마다 dictionary 비우기
        dic_menus.clear()
        # 주문한 메뉴들 체크
        for menu in orders:
            # 메뉴 개수만큼 경우의 수 모두 체크(중복 X, 순서는 바뀔 수 있으니 정렬해서 dictionary에 추가)
            for item in combinations(sorted(menu), length):
                # default가 0이기 때문에 선언 없이 바로 증감 가능
                dic_menus[item] += 1
        # 메뉴를 주문된 수만큼 내림차순 정렬
        arr = sorted(dic_menus.keys(), key=lambda x: -dic_menus[x])
        # 비어있거나 1번 주문된 주문들은 제외
        if not arr or dic_menus[arr[0]] == 1:
            continue
        # 튜플을 Sring 으로 변환
        s = ""
        for i in range(len(arr[0])):
            s += arr[0][i]
        # 처음은 그냥 넣기
        answer.append(s)
        # 혹시 공동 1등있나 확인
        for i in range(1, len(arr)):
            if dic_menus[arr[i]] != dic_menus[arr[i - 1]]:
                break
            else:
                # 있으면 추가
                s = ""
                for j in range(len(arr[i])):
                    s += arr[i][j]
                answer.append(s)
    # 마지막 정렬
    answer.sort()
    return answer

```

## [민웅](./메뉴%20리뉴얼/민웅.py)

```py

```

## [병국](./메뉴%20리뉴얼/병국.py)

```py

```

## [상미](./메뉴%20리뉴얼/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 블로그

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./블로그/성구.py)

```py
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
```

## [민웅](./블로그/민웅.py)

```py
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
```

## [병국](./블로그/병국.py)

```py
# 틀렸습니다 2% ...
n,x = map(int,input().split())
arr = list(map(int,input().split()))
maxx = sum(arr[:x])
cnt = 1

for i in range(x,n):
    plus = arr[i] - arr[i-x]
    if plus < 0:
        pass
    elif plus == 0:
        cnt += 1
    else:
        maxx += plus
        cnt = 1
if maxx == 0:
    print("SAD")
else:
    print(maxx)
print(cnt)



```

## [상미](./블로그/상미.py)

```py
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
```

</div>
</details>

<br/><br/><br/>

# [백준] 회전 초밥

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./회전%20초밥/성구.py)

```py
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

```

## [민웅](./회전%20초밥/민웅.py)

```py
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

```

## [병국](./회전%20초밥/병국.py)

```py
n,d,k,c = map(int,input().split())
#접시, 초밥가짓수, 연속접시수, 쿠폰번호

bob_li = []
for _ in range(n):
    bob = int(input())
    bob_li.append(bob)

maxx = 0
for i in range(len(bob_li)):
    if i+k <= len(bob_li):
        if c in bob_li[i:i+k]:
            maxx = max(maxx,len(set(bob_li[i:i+k])))
        else:
            maxx = max(maxx,len(set(bob_li[i:i+k]))+1)
    else:
        new = bob_li[i:]+bob_li[:i+k-len(bob_li)]
        if c in new:
            maxx = max(maxx,len(set(new)))
        else:
            maxx = max(maxx,len(set(new))+1)
print(maxx)

```

## [상미](./회전%20초밥/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 탑보기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./탑보기/성구.py)

```py

```

## [민웅](./탑보기/민웅.py)

```py
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
```

## [병국](./탑보기/병국.py)

```py

```

## [상미](./탑보기/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>
