import sys
input = sys.stdin.readline

n,m=map(int,input().split())

arr=list(map(int,input().split()))

# 찾는값 : 절단기 위치
answer=[]
def binary(l,r):

    while l <= r:
        
        mid = (l+r)//2

        sum = 0
        for i in arr:
            if i >= mid:
                sum += i-mid        
        
        if sum < m:
            r = mid -1
        else:
            answer.append(mid)
            l = mid + 1
        


l = 1
r = max(arr)

binary(l,r)
if answer:
    print(max(answer))
else:
    print(0)