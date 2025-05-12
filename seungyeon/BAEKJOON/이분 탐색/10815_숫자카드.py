import sys
input=sys.stdin.readline

n=int(input().strip())
arr=list(map(int,input().split()))
m=int(input().strip())
check=list(map(int,input().split()))

arr.sort()
# 이분탐색 함수
def binary(x):

    l,r=0,n-1
    
    k=False

    while l <= r:

        p = (l+r) //2 

        if arr[p] == x:
            k = True
            break
        
        if arr[p] > x :
            r = p -1
        else:
            l = p + 1

    return k


answer=[]
for i in range(m):
    print(1 if binary(check[i]) else 0, end=' ')
