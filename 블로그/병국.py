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


