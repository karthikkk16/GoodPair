def goodpair(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                return 1
    return 0

a=list(map(int,input().split()))
k=int(input())
print(goodpair(a,k))
