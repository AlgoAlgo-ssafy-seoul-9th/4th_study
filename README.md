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

```

## [상미](./블로그/상미.py)

```py

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

```

## [민웅](./회전%20초밥/민웅.py)

```py

```

## [병국](./회전%20초밥/병국.py)

```py

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
