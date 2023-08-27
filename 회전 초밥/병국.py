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
