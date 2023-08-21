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


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
